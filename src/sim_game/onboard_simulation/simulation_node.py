#!/usr/bin/env python

import config as cfg
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
		self.roomba_topic_store = None

		# Robot Attributes
		# self.rbaList_msg = None
		# self.rbaList_msg_old = None

		# Probability
		self.delta = None
		self.XYR = []

		# Display Attributes
		self.agent = None
		self.headerLabels = ['Label1: ', 'Label2: ', 'Label3: ']
		self.headerArgs = [0.0,0.0,0.0]

	def set_delta(self, delta):
		self.delta = delta

	def store_msg(self):
		if len(self.roomba_topic.roombaList) == 0:
			return
		else:
			self.roomba_topic_store = self.roomba_topic 

	def roomba_callback(self, topic):
		self.store_msg()
		self.roomba_topic = topic
		self.compare_msgs()
		self.set_delta(topic.delta)

	def compare_msgs(self):
		if self.roomba_topic_store == None:
			return

		max = len(self.roomba_topic.roombaList)
		for i in range(max-1):

			# If was detected and now not
			if (not self.roomba_topic.roombaList[i].detected and self.roomba_topic_store.roombaList[i].detected):
				# Store (pos,r) in list
				self.XYR[i] = (self.roomba_topic_store.roombaList[i].x, self.roomba_topic_store.roombaList[i].y, cfg.ROOMBA_MIN_RADIUS)
			elif (not self.roomba_topic.roombaList[i].detected):
				xyr = self.XYR[i]
				x = xyr[0]
				y = xyr[1]
				radius = xyr[2] + cfg.ROOMBA_LINEAR_SPEED * self.delta
				self.XYR[i] = (x,y,radius)

			elif self.roomba_topic.roombaList[i].detected:
				self.XYR[i] = (0.0,0.0,0.0)
			elif self.roomba_topic.roombaList[i].r >= cfg.ROOMBA_MAX_RADIUS:
				self.XYR[i] = (0.0,0.0,0.0)

	def get_roomba_data(self):
		return self.roomba_topic

	def get_delta(self):
		return self.delta

	def setup(self):
		self.ROS._callback = self.roomba_callback
		self.ROS.create_listener('roomba_msgs', self.roomba_callback, roombaList_msg)
		self.setup_probList()

	def setup_probList(self):
		x = 0
		y = 0
		r = 0
		prob = (x,y,r)
		self.XYR = [prob]*14
