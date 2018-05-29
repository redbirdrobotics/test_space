'''
#!/usr/bin/env python

import util
from ROSExtension import ROSExtension
import rospy
from sim_game.msg import fake_localization, fake_localization_map, FC_Roombas, FC_Roombas_Map, SimMap
from roomba import Roomba, Obstacle_Roomba
from math import sqrt
import numpy as np
#from drone_loc import DroneLoc

class Differentiate_Roombas(object):
	
	def __init__(self):

		self.list_of_active_roombas = []

		self.list_of_obstacle_roombas = []

		for i in range(4):
			theta = (2*np.pi * i) / 4

			obstacle_roomba = Obstacle_Roomba(
				[np.cos(theta) * 5 + 10, np.sin(theta) * 5 + 10],
				theta - (np.pi / 2),
				i
			)

		self.list_of_obstacle_roombas.append(obstacle_roomba)

		self.FC_roombas_to_be_sent = []

   		self.ros = ROSExtension()
		
		self.ros.init_ros_node('Diff_And_Prob')

		self.ros.create_listener('Target_Roomba', self.callback_for_localization_msg, fake_localization_map)

		self.fc_pub = self.ros.create_publisher('FOV_Roombas', FC_Roombas_Map)

		self.pub = self.ros.create_publisher('Probability_Message', SimMap)

		#self.droneLoc = DroneLoc()
		
		self.drone_coors = None

		self.current_message = None

		self.previous_message = None

	def scan_message_for_old_robots(self):

		if self.previous_message is None:

			return

		for old_message in self.previous_message.localization_map:

			if not old_message.active:

				continue

			else:

				index = 0

				for new_message in self.current_message.localization_map:

					delta = float( self.current_message.header.stamp.secs - self.previous_message.header.stamp.secs ) + float(self.current_message.header.stamp.nsecs - self.previous_message.header.stamp.nsecs) / 1000000000

					if sqrt(( (old_message.x - new_message.x)**2 + (old_message.y - new_message.y)**2 )) < (delta * 0.33) :

						#rospy.loginfo(sqrt((old_message.x - new_message.x)**2 + (old_message.y - new_message.y)**2) < delta*0.33 )

						new_message.v_x, new_message.v_y = ( new_message.x - old_message.x )  / delta , ( new_message.y - old_message.y )  / delta

						new_message.checked, new_message.active = True, True

						fc_msg = FC_Roombas()

						fc_msg.x, fc_msg.y = new_message.x, new_message.y

						fc_msg.v_x, fc_msg.v_y = new_message.v_x, new_message.v_y

						#rospy.loginfo(new_message)

						self.FC_roombas_to_be_sent.append(fc_msg)

					else:

						roomba = Roomba()

						roomba.pos = (new_message.x, new_message.y)

						roomba.id = new_message.id

						self.update_active_roombas(roomba)

					index+=1


	def backup_old_message(self, new_message):

		if not len(new_message.localization_map) == 0:

			self.previous_message = self.current_message

		self.current_message = new_message

	def package_and_send_msg(self):

		#rospy.loginfo(diffMsg)

		FCMsg = FC_Roombas_Map()

		FCMsg.target_roombas = self.FC_roombas_to_be_sent

		self.fc_pub.publish(FCMsg)

		rospy.loginfo(FCMsg)

		self.FC_roombas_to_be_sent = []

	def callback_for_localization_msg(self, incoming_message):

		#rospy.loginfo(incoming_message)

		self.backup_old_message(incoming_message)

		self.scan_message_for_old_robots()

		self.package_and_send_msg()

	def update_active_roombas(self, roomba):

        	for target in self.list_of_active_roombas:

            	    if util.circle_intersects_circle(target.pos, roomba.pos, roomba.max_radius):

                	self.collided(roomba, target)

            	    if(util.circle_intersects_goal(roomba.pos, roomba.max_radius)):

                	roomba.exceeds_boundary['goal_line'] = True

                	roomba.time_to_look = util.min_time(roomba.pos, 0)

            	    if(util.circle_intersects_rboundary(roomba.pos, roomba.max_radius)):

                	roomba.exceeds_boundary['right_boundary'] = True

                	roomba.time_to_look = util.min_time(roomba.pos, 1)

                    if(util.circle_intersects_bboundary(roomba.pos, roomba.max_radius)):

                	roomba.exceeds_boundary['bottom_boundary'] = True

                	roomba.time_to_look = util.min_time(roomba.pos, 2)

                    if(util.circle_intersects_lboundary(roomba.pos, roomba.max_radius)):

                	roomba.exceeds_boundary['left_boundary'] = True

                	roomba.time_to_look = util.min_time(roomba.pos, 3)

        	self.list_of_active_roombas.append(roomba)

        	#rospy.loginfo(len(self.list_of_active_roombas))

    	def collided(self, roomba_a, roomba_b):

        	roomba_a.ids_of_collision.append(roomba_b.id)

        	roomba_b.ids_of_collision.append(roomba_a.id)

    	def publish_message(self):

        	TRmsgMap = []

        	ORmsgMap = []

        	roombaMap = SimMap()

        	for roomba in self.list_of_active_roombas:

            	    TRmsgMap.append(roomba.ros_msg_type)
        
            	    #rospy.loginfo(roomba.ros_msg_type)

        	for roomba in self.list_of_obstacle_roombas:

            	    ORmsgMap.append(roomba.ros_msg_type)

            	    #rospy.loginfo(roomba.ros_msg_type)

        	roombaMap.target_robots, roombaMap.obstacle_robots = TRmsgMap, ORmsgMap

        	self.pub.publish(roombaMap)

    	def start_sim(self):

        	index_to_remove = []

        	index = 0

        	while not rospy.is_shutdown():

        		if not len(self.list_of_active_roombas) == 0:

	            	    for roomba in self.list_of_active_roombas:

	                	if roomba._probability > 0:

	                             roomba.update()

	                	else:

	                    	     #rospy.loginfo('i am deleting bad robots')

	                    	     index_to_remove.append(index)

	                    index+=1

	            	    for roomba in self.list_of_obstacle_roombas:

	                	roomba.update()

	            	    for index in index_to_remove:

	                	del self.list_of_active_roombas[index]

	            	self.publish_message()

	            	index = 0

	            	index_to_remove = []

	            	rospy.sleep(1)

	def loop_till_ros_ends(self):
		
		rospy.spin()


if __name__ == '__main__':
	
	Diff = Differentiate_Roombas()

	Diff.start_sim()
'''