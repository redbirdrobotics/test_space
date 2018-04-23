#!/usr/bin/env python

from communication import ROSExtension
from sim_game.msg import roomba_msg, roombaList_msg
from robots import roomba
import rospy

class Simulation_Node(object):

	def __init__(self):

		# ROS Attributes
		self.ROS = ROSExtension()
		self.ROS.init_ros_node('Simulation_Node')
		self.ROS._pub = None
		self.ROS._callback = None
		self.ROS._listen = None

		# Subscriber Attributes
		self.roomba_topic = roombaList_msg()

		# Robot Attributes
		self.rbaList_msg = None

		# Display Attributes
		self.agent = None
		self.headerLabels = ['Label1: ', 'Label2: ', 'Label3: ']
		self.headerArgs = [0,0,0]

	def roomba_callback(self, topic):
		self.roomba_topic = topic

	def get_roomba_data(self):
		return self.roomba_topic

	def setup(self):
		self.ROS._callback = self.roomba_callback
		self.ROS.create_listener('roomba_msgs', self.roomba_callback, roombaList_msg)

	def update(self):
		return self.roomba_topic




