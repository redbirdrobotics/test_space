#!/usr/bin/env python

import config as cfg
from communication import ROSExtension
#from sim_game.msg import roomba_msg, roombaList_msg
from sim_game.msg import FC_Roombas, FC_Roombas_Map, SimMap, obstacle_roomba, Sim, fake_localization_map
from robots import roomba
import rospy

class Tmp_Simulation_Node(object):

	def __init__(self):

		# ROS Attributes
		self.ROS = ROSExtension()
		self.ROS.init_ros_node('Simulation_Node')
		self.ROS.diff_pub = None
		self.ROS.sim_pub = None
		self.ROS._callback = None
		self.ROS._listen = None

		# Subscriber Attributes
		self.roomba_topic = SimMap()
		self.roomba_topic_store = None

		# Robot Attributes
		# self.rbaList_msg = None
		# self.rbaList_msg_old = None

		# Probability
		self.delta = None
		self.XYR = []

		# Display Attributes
		self.agent = None
		self.headerLabels = ['DiffMsg: ', 'SimMsgTRLen: ', 'SimMsgORLen: ', 'EnvMsg: ']
		self.headerArgs = [0.0,0.0,0.0,0.0]

		self.tr_msg_prob = [Sim()]
		self.or_msg_prob = [obstacle_roomba()]

		self.tr_msg_diff = [FC_Roombas()]

	def set_delta(self, delta):
		self.delta = delta

	def get_delta(self):

		return self.delta

	def get_roomba_data(self):

		return self.roomba_topic

	def callback_for_roombas_from_prob(self, msg):

		#rospy.loginfo('callback for prob')

		self.tr_msg_prob, self.or_msg_prob = msg.target_robots, msg.obstacle_robots

		self.headerArgs[1], self.headerArgs[2] =  len(msg.target_robots), len(msg.obstacle_robots)

	def get_prob_msgs(self):

		return self.tr_msg_prob, self.or_msg_prob
			
	def callback_for_roombas_from_diff(self, msg):

		#rospy.loginfo(msg)

		self.tr_msg_diff = msg.target_roombas

		self.headerArgs[0] = len(msg.target_roombas)

	def get_diff_msg(self):

		return self.tr_msg_diff

	def set_delta(self, delta):

		self.detla = delta

	def callback_for_roombas_from_env(self, ros_msg):

		self.headerArgs[3] = len(ros_msg.localization_map)

	def setup(self):

		self.ROS.create_listener('Probability_Message', self.callback_for_roombas_from_prob, SimMap) 

		self.ROS.create_listener('FOV_Roombas', self.callback_for_roombas_from_diff, FC_Roombas_Map)

		self.ROS.create_listener('Target_Roomba', self.callback_for_roombas_from_env, fake_localization_map)