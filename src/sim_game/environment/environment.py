#!/usr/bin/env python

'''
environment.py

Contains an Environment class that can be used to
setup initial configurations and perform game-wide
update steps.

Additionally, this class is responsible for performing
collision detection and notifying child roombas via
the collision dict.
'''

import numpy as np
import rospy

import geometry
import config as cfg
from robots import roomba
from communication import ROSExtension
#from sim_game.msg import roomba_msg, roombaList_msg
from sim_game.msg import fake_localization_map, fake_localization

class Environment(object):
    
    '''
    A class to represent a game round.

    Contains methods to initialize a round and update
    methods that can be used to progress through time.
    '''

    def __init__(self):
        self.roombas = []
        self.agent = None
        self.good_exits = 0
        self.bad_exits = 0
        self.score = 0
        self.target_roomba = None
        self.target_type = None

    def make_node(self):
        self.ros = ROSExtension()
        self.ros.init_ros_node('Demo_Node')
        self.ros.create_publisher('Target_Roomba', fake_localization_map)

    def reset(self):
        '''
        Spawns roombas and positions them as follows:

        - 10 target roombas evenly spaced around a 1m circle
        centered at the origin. All roombas initially face
        outwards.

        - 4 obstacle roombas evenly spaced around a 4m circle
        centered at the origin. Roombas move clockwise around
        the circle.
        '''
        self.roombas = []
        self.agent = None
        self.good_exits = 0
        self.bad_exits = 0
        self.score = 0
        self.target_roomba = None
        self.target_type = None
        self.activeRoombas = []

        # spawn target roombas
        for i in range(cfg.MISSION_NUM_TARGETS):
            theta = (cfg.TAU * i) / cfg.MISSION_NUM_TARGETS

            target_roomba = roomba.TargetRoomba(
                [np.cos(theta) * cfg.MISSION_TARGET_SPAWN_RADIUS + 10, np.sin(theta) * cfg.MISSION_TARGET_SPAWN_RADIUS + 10],
                theta,
                tag=i
            )

            target_roomba.start()

            self.roombas.append(target_roomba)

        # spawn obstacle roombas
        for i in range(cfg.MISSION_NUM_OBSTACLES):
            theta = (cfg.TAU * i) / cfg.MISSION_NUM_OBSTACLES

            obstacle_roomba = roomba.ObstacleRoomba(
                [np.cos(theta) * cfg.MISSION_OBSTACLE_SPAWN_RADIUS + 10, np.sin(theta) * cfg.MISSION_OBSTACLE_SPAWN_RADIUS + 10],
                theta - (cfg.PI / 2),
                tag=9+i
            )

            obstacle_roomba.start()

            self.roombas.append(obstacle_roomba)

    '''
    def populate_msg(self, delta):
        i = 0
        List_msg = roombaList_msg()
        for roomba in self.roombas:
            i += 1
            msg = roomba_msg()
            msg.id = i
            msg.x = roomba.pos[0]
            msg.y = roomba.pos[1]
            if roomba.state == cfg.ROOMBA_STATE_IDLE:
                msg.removed = True

            msg.detected = roomba.detected
            if msg.detected:
                msg.static_x = roomba.pos[0]
                msg.static_y = roomba.pos[1]
                msg.r = 0
            else:
                msg.r += cfg.ROOMBA_LINEAR_SPEED * delta
            List_msg.roombaList.append(msg)
            List_msg.delta = delta
        self.ros.send_msg(List_msg)
    '''

    def populate_msg(self, elapsed):

        msgMap = []

        roombaList = fake_localization_map()

        roombaList.elapsed = elapsed

        for roomba in self.roombas:

            if roomba.detected:

                msg = fake_localization()

                msg.x, msg.y = roomba.pos

                msg.id = roomba.tag

                msg.checked, msg.active = False, True

                msgMap.append(msg)

        roombaList.localization_map = msgMap

        self.ros.send_msg(roombaList)

        #rospy.loginfo(roombaList)
            

    def update(self, delta, elapsed):
        '''
        Perform an update step.

        This will update all child roombas and perform collision
        detection in O(n^2) time. At the current stage, this is
        "good enough" for realtime display but for high-speed
        simulation in a neural network training phase it may
        make sense to improve the efficiency of certain aspects
        of the code.
        '''

        curr_count = 0

        grand_count = 0

        # Loop through all roombas
        for i in range(len(self.roombas)):
            rba = self.roombas[i]

            # ignore roombas that left the arena
            if (rba.state == cfg.ROOMBA_STATE_IDLE):
                rba.detected = False
                continue

            rba.update(delta, elapsed)

            # Perform roomba-to-roomba collision detection
            for j in range(len(self.roombas)):
                # ignore self collisions and collisions with roombas that left
                if i == j or self.roombas[j].state == cfg.ROOMBA_STATE_IDLE:
                    continue

                if Environment._check_roomba_collision(rba, self.roombas[j]):
                    if Environment._check_roomba_is_facing(rba, self.roombas[j].pos):
                        rba.collisions['front'] = True

            # Perform FOV detection
            if self.agent.detects_roomba(rba):
                rba.detected = True
            else:
                rba.detected = False

            # Perform drone-to-roomba collision detection
            if self.agent.is_touching_roomba_top(rba):
                rba.collisions['top'] = True

            if self.agent.is_blocking_roomba(rba):
                if Environment._check_roomba_is_facing(rba, self.agent.xy_pos):
                    rba.collisions['front'] = True

            # Check if the roomba has left the arena
            (has_left, reward) = Environment._check_bounds(rba)
            if has_left:
                print('roomba left, reward: ' + str(reward))
                if reward > 0:
                    self.good_exits += 1
                else:
                    self.bad_exits += 1
                self.score += reward
                rba.stop()

            grand_count+=1

            if grand_count == 14:

                if not len(self.activeRoombas) == 0:
                
                    self.ros_target_roomba.populate_publish_tr_msg(self.activeRoombas)

                    self.ros_target_roomba.logInfo('populating the msg')

                curr_count = 0

                grand_count = 0

                del self.activeRoombas[:]

        self.populate_msg(elapsed)

        # update the drone
        self.agent.update(delta, elapsed)

    @staticmethod
    def _check_roomba_collision(ra, rb):
        '''
        Returns true if two roombas are touching.

        The calculation is done purely by determining the
        euclidean distance and comparing that to the radius
        of each roomba.
        '''
        return geometry.circle_intersects_circle(ra.pos, rb.pos, cfg.ROOMBA_RADIUS)

    @staticmethod
    def _check_roomba_is_facing(ra, pos):
        '''
        Returns true if roomba ra is facing the point pos.

        This works by determining the angle of the vector
        ra -> pos relative to the +x axis and checking if the
        heading of ra is within pi/2 radians of that result.
        '''
        ang = np.arctan2(pos[1] - ra.pos[1], pos[0] - ra.pos[0])
        return geometry.compare_angle(ra.heading, ang) < cfg.PI / 2

    @staticmethod
    def _check_bounds(r):
        '''
        Check if a roomba has left the arena.

        Returns (has_left, reward):

        has_left - True if the roomba is outside the arena
        reward - 1 only if the roomba crossed the goal line,
            0 otherwise
        '''
        has_left = False
        reward = -1000

        if (r.pos[0] < -cfg.ROOMBA_RADIUS
            or r.pos[1] < -cfg.ROOMBA_RADIUS
            or r.pos[0] > 20 + cfg.ROOMBA_RADIUS
            or r.pos[1] > 20 + cfg.ROOMBA_RADIUS):
            has_left = True

        if (r.pos[0] > 20 + cfg.ROOMBA_RADIUS):
            reward = 2000

        return (has_left, reward)
