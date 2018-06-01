#!/usr/bin/env python
import differentiation
import util
from ROSExtension import ROSExtension
#from drone_loc import DroneLoc
import rospy
from sim_game.msg import fake_localization, fake_localization_map, FC_Roombas, FC_Roombas_Map
from math import sqrt
#from drone_loc import DroneLoc

class Differentiate_Roombas(object):

	def __init__(self):

		self.primed_ros_extension = ROSExtension()

		self.primed_ros_extension.init_ros_node('Differentiation_Simulation')

		self.primed_ros_extension.create_listener('Target_Roomba', self.callback_for_localization_msg, fake_localization_map)

		self.fc_pub = self.primed_ros_extension.create_publisher('FOV_Roombas', FC_Roombas_Map)

		self.sim_pub = self.primed_ros_extension.create_publisher('Differentiate_Roombas', fake_localization_map)

		self.FC_Roombas_To_Send = []

		self.previous_message = None

		self.previous_roombas = None

		self.current_message = None

		self.current_roombas = None

		#self.DroneLoc = DroneLoc()

	def callback_for_localization_msg(self, incoming_roombas):

		self.backup_msg(incoming_roombas)

		self.scan_for_old_roombas()

		self.send_all_messages()

		self.FC_Roombas_To_Send = []

	def backup_msg(self, incoming_roombas):

		self.previous_message = self.current_message

		self.current_message = incoming_roombas

		self.backup_roombas()

	def backup_roombas(self):

		if self.previous_message is not None:

			self.previous_roombas = self.previous_message.localization_map

			for previous_roomba in self.previous_roombas:

				previous_roomba.active = False

		self.current_roombas = self.current_message.localization_map

	def scan_for_old_roombas(self):

		if self.previous_message is not None:

			already_active_roombas = []

			for current_roomba in self.current_roombas:

				#already_active_roombas = self.scan_for_similarity_in_old_roombas(current_roomba, already_active_roombas)

				for  index in range(len(self.previous_roombas)):

					previous_roomba = self.previous_roombas[index]

					if index in already_active_roombas:

						continue

					time_elapsed_bw_messages = self.current_message.elapsed - self.previous_message.elapsed

					distance_in_x = ( current_roomba.x - previous_roomba.x )

					distance_in_y = ( current_roomba.y - previous_roomba.y )

					actual_distance_traveled = sqrt( pow( distance_in_x , 2 ) + pow( distance_in_y , 2 ) )

					previous_roomba.v_x, previous_roomba.v_y = distance_in_x / time_elapsed_bw_messages, distance_in_y / time_elapsed_bw_messages

					max_possible_distance_traveled = 0.33 * time_elapsed_bw_messages

					#print 'actual_distance_traveled %s' % actual_distance_traveled

					#print 'max_possible_distance_traveled %s' % max_possible_distance_traveled

					if actual_distance_traveled <= max_possible_distance_traveled:

						previous_roomba.active = True

						already_active_roombas.append(index)

						self.package_fc_roombas(previous_roomba)

						break

		else:

			self.send_only_new_roombas()

	def scan_for_similarity_in_old_roombas(self, current_roomba, already_active_roombas):

		index = 0

		for previous_roomba in self.previous_roombas:

			if index in already_active_roombas:

				continue

			time_elapsed_bw_messages = self.current_message.elapsed - self.previous_message.elapsed

			distance_in_x = ( current_roomba.x - previous_roomba.x )

			distance_in_y = ( current_roomba.y - previous_roomba.y )

			actual_distance_traveled = sqrt( pow( distance_in_x , 2 ) + pow( distance_in_y , 2 ) )

			previous_roomba.v_x, previous_roomba.v_y = distance_in_x / time_elapsed_bw_messages, distance_in_y / time_elapsed_bw_messages

			max_possible_distance_traveled = time_elapsed_bw_messages * 0.33

			#print 'actual_distance_traveled %s' % actual_distance_traveled

			#print 'max_possible_distance_traveled %s' % max_possible_distance_traveled

			if actual_distance_traveled <= max_possible_distance_traveled:

				previous_roomba.active = True

				already_active_roombas.append(index)

				index+=1

				self.package_fc_roombas(previous_roomba)

				break

			index+=1

		return already_active_roombas

	def send_only_new_roombas(self):

		for current_roomba in self.current_roombas:

			self.package_fc_roombas(current_roomba)

	def package_fc_roombas(self, roomba_to_send):

		#quadX, quadY = self.DroneLoc.get_coors()

		fc_msg = FC_Roombas()

		fc_msg.x, fc_msg.y, fc_msg.v_x, fc_msg.v_y = roomba_to_send.x, roomba_to_send.y, roomba_to_send.v_x, roomba_to_send.v_y

		self.FC_Roombas_To_Send.append(fc_msg)

	def send_all_messages(self):

		if self.previous_message is not None:

			sim_msg = []

			for previous_roomba in self.previous_roombas:

				if not previous_roomba.active:

					sim_msg.append(previous_roomba)

			sim_msg_map = fake_localization_map()

			sim_msg_map.localization_map = sim_msg

			self.sim_pub.publish(sim_msg_map)

			if len(sim_msg) > 0:

				rospy.loginfo('there is an inactive roomba!!!!')

		fc_msg_map = FC_Roombas_Map()

		fc_msg_map.target_roombas = self.FC_Roombas_To_Send

		self.fc_pub.publish(fc_msg_map)

if __name__ == '__main__':

	Diff = Differentiate_Roombas()
	
	rospy.spin()

