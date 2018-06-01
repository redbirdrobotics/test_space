#!/usr/bin/env python

from roomba import Roomba, Obstacle_Roomba

from ROSExtension import ROSExtension
import util
from sim_game.msg import SimMap, fake_localization, fake_localization_map
import rospy
import numpy as np

class On_Board_Sim():

    def __init__(self):


        self.list_of_unactive_roombas = []

        self.list_of_obstacle_roombas = []

        for i in range(4):
            theta = (2*np.pi * i) / 4

            obstacle_roomba = Obstacle_Roomba(
                [np.cos(theta) * 5 + 10, np.sin(theta) * 5 + 10],
                theta - (np.pi / 2),
                i
            )

            self.list_of_obstacle_roombas.append(obstacle_roomba)

        self.ros = ROSExtension()

        self.ros.init_ros_node('On_Board_Simulation')

        self.ros.create_listener('Differentiate_Roombas', self.listener_for_roombas, fake_localization_map)

        self.pub = self.ros.create_publisher('Probability_Message', SimMap)

    def listener_for_roombas(self, ros_msg):

        if len(ros_msg.localization_map) > 0:

            for msg in ros_msg.localization_map:
                
                ground_roomba = Roomba()

                ground_roomba.pos = ( msg.x, msg.y )

                ground_roomba.id = msg.id

                self.update_active_roombas(ground_roomba)

    def update_active_roombas(self, roomba):

        if len(self.list_of_unactive_roombas) > 0:

            for target in self.list_of_unactive_roombas:

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

            self.list_of_unactive_roombas.append(roomba)

        else:

            self.list_of_unactive_roombas.append(roomba)

        #rospy.loginfo(len(self.list_of_unactive_roombas))

    def manage_active_robots(self):

        index_to_remove = []

        index = 0

        rospy.loginfo( len(self.list_of_unactive_roombas) )

        for rba in self.list_of_unactive_roombas:

            if rba._probability <= 0:

                index_to_remove.append(index)

            index += 1

        for i in index_to_remove:

            rospy.loginfo( 'index 2' )

            rospy.loginfo( i )

            del self.list_of_unactive_roombas[i]

    def collided(self, roomba_a, roomba_b):

        roomba_a.ids_of_collision.append(roomba_b.id)

        roomba_b.ids_of_collision.append(roomba_a.id)

    def publish_message(self):

        TRmsgMap = []

        ORmsgMap = []

        roombaMap = SimMap()

        for roomba in self.list_of_unactive_roombas:

            TRmsgMap.append(roomba.ros_msg_type)
        
            #rospy.loginfo(roomba.ros_msg_type)

        for roomba in self.list_of_obstacle_roombas:

            ORmsgMap.append(roomba.ros_msg_type)

            #rospy.loginfo(roomba.ros_msg_type)

        roombaMap.target_robots, roombaMap.obstacle_robots = TRmsgMap, ORmsgMap

        self.pub.publish(roombaMap)

        #rospy.loginfo(roombaMap)

    def start_sim(self):

        while not rospy.is_shutdown():

            for roomba in self.list_of_unactive_roombas:

                if roomba._probability > 0:

                    roomba.update()

                    self.manage_active_robots()

            for roomba in self.list_of_obstacle_roombas:

                roomba.update()

            self.publish_message()

            rospy.sleep(1)

if __name__ == '__main__':

    Sim = On_Board_Sim()

    Sim.start_sim()