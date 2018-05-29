#!/usr/bin/env python
import differentiation
import util
from ROSExtension import ROSExtension
import rospy
from sim_game.msg import fake_localization, fake_localization_map, FC_Roombas, FC_Roombas_Map
from math import sqrt
#from drone_loc import DroneLoc


if __name__ == '__main__':
	
	primed_ros_extension = ROSExtension()

	primed_ros_extension.init_ros_node('Differentiation_Simulation')

	primed_ros_extension.create_listener('Target_Roomba', self.callback_for_localization_msg, fake_localization_map)

	fc_pub = primed_ros_extension.create_publisher('FOV_Roombas', FC_Roombas_Map)

	sim_pub = primed_ros_extension.create_publisher('Differentiate_Roombas', fake_localization_map)

	Diff = Differentiate_Roombas(primed_ros_extension, sim_pub, fc_pub)
	
	rospy.spin()

