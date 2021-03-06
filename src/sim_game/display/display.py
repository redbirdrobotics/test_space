'''
display.py

Contains a Display class which can be used to visualize
a mission round.

The graphics are entirely decoupled from the simulation
engine and this file contains all the implementations
of the drawing methods.

Graphics are drawn to the screen using pyglet as an
OpenGL interface. This should provide realtime-capable
graphics as well as relatively cross-platform availability.
'''
import pyglet
from pyglet.gl import *
import numpy as np
import time

from sim_game.msg import fake_localization, Sim

import config as cfg
from robots import roomba
import geometry

class Env_Display(pyglet.window.Window):

    def __init__(self, environment, timescale=1.0, self_update=True):
        super(Env_Display, self).__init__(700,700)

        self._timescale = timescale
        self.update_func = (lambda a,b:0)
        self._click_callback = (lambda a,b:None)
        self._paused = False
        self._elapsed = 0.0

        if self_update:
            pyglet.clock.schedule_interval(self._update, 1.0/self._timescale/60.0)
            pyglet.clock.set_fps_limit(self._timescale*60)

        self.environment = environment
        self.start_time = time.time()

    def set_click_callback(self, callback):
        self._click_callback = callback

    def set_update_func(self, update_func):
        self.update_func = update_func

    def _update(self, dt):
        if not self._paused:
            self._elapsed += dt * 1000
            self.update_func(self._timescale*dt, self._timescale*self._elapsed)

    def on_resize(self, width, height):
        glViewport(10, 10, width-20, height-20)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 20, 0, 20, -1, 1)

        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glEnable( GL_BLEND );

    def on_draw(self):
        pyglet.clock.tick()
        glClear(GL_COLOR_BUFFER_BIT)

        Env_Display._draw_gridlines()

        self._draw_header(self.environment.good_exits,
                          self.environment.bad_exits,
                          self.environment.score,
                          int(self._elapsed / 1000))

        for r in self.environment.roombas:
            if isinstance(r, roomba.TargetRoomba):
                if self.environment.target_roomba == r.tag:
                    Env_Display._draw_target_roomba(r, self.environment.target_type)
                else:
                    Env_Display._draw_target_roomba(r)
            else:
                Env_Display._draw_obstacle_roomba(r)

        Env_Display._draw_drone(self.environment.agent)

    def on_mouse_release(self, x, y, button, modifiers):
        x = (x - 10) * 20.0 / (self.get_size()[0] - 20.0)
        y = (y - 10) * 20.0 / (self.get_size()[1] - 20.0)
        for r in self.environment.roombas:
            if isinstance(r, roomba.TargetRoomba):
                if np.hypot(x - r.pos[0], y - r.pos[1]) < cfg.ROOMBA_RADIUS:
                    self._click_callback(r,
                                         'left'
                                         if button == pyglet.window.mouse.LEFT
                                         else 'right')
                    break
        else:
            self._click_callback((x, y),
                                 'left'
                                 if button == pyglet.window.mouse.LEFT
                                 else 'right')

    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self._paused = not self._paused

    @staticmethod
    def _draw_target_roomba(r, special_state=None):
        pos = r.pos
        heading = r.heading
        vertex_count = cfg.GRAPHICS_CIRCLE_VERTICES
        radius = cfg.ROOMBA_RADIUS

        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

        # Outline
        if special_state == 'hitting':
            glColor3f(0.7, 0.7, 1.0)
        elif special_state == 'blocking':
            glColor3f(0.7, 1.0, 0.7)
        elif r.state == cfg.ROOMBA_STATE_FORWARD:
            glColor3f(1,1,1)
        elif r.state in (cfg.ROOMBA_STATE_TURNING_NOISE,
                         cfg.ROOMBA_STATE_REVERSING,
                         cfg.ROOMBA_STATE_TOUCHED):
            glColor3f(1,0.8,0.8)

        Env_Display._draw_hollow_circle(pos, radius)

        # Direction indicator
        glBegin(GL_LINES)

        glVertex2f(pos[0], pos[1])
        glVertex2f(np.cos(heading) * radius + pos[0], np.sin(heading) * radius + pos[1])

        glEnd()

    @staticmethod
    def _draw_obstacle_roomba(r):
        pos = r.pos
        heading = r.heading
        vertex_count = cfg.GRAPHICS_CIRCLE_VERTICES
        radius = cfg.ROOMBA_RADIUS

        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

        # Outline
        if r.state == cfg.ROOMBA_STATE_FORWARD or True:
            glColor3f(1,0.2,0.2)
        elif r.state == cfg.ROOMBA_STATE_TURNING:
            glColor3f(1,0.8,0.8)

        Env_Display._draw_hollow_circle(pos, radius)

        # Direction indicator
        glBegin(GL_LINES)

        glVertex2f(pos[0], pos[1])
        glVertex2f(np.cos(heading) * radius + pos[0], np.sin(heading) * radius + pos[1])

        glEnd()

    @staticmethod
    def _draw_drone(drone):
        if cfg.RENDER_AGENT != None:
            cfg.RENDER_AGENT(drone)

    def _draw_header(self, good, bad, score, elapsed_secs):
        mins = elapsed_secs // 60
        secs = elapsed_secs % 60
        self.set_caption(
            'Time: %02d:%02d  Good exits: %d   Bad exits: %d   Score: %d'%(
                mins,
                secs,
                good,
                bad,
                score))

    @staticmethod
    def _draw_gridlines():

        # draw horizontal lines
        for y in range(0,21):
            if y % 5 == 0:
                glColor3f(0.5,0.5,0.5)
            else:
                glColor3f(0.25,0.25,0.25)

            glBegin(GL_LINES)
            glVertex2f(0,y)
            glVertex2f(20,y)
            glEnd()

        # draw vertical lines
        for x in range(1,20):
            if x % 5 == 0:
                glColor3f(0.5,0.5,0.5)
            else:
                glColor3f(0.25,0.25,0.25)

            glBegin(GL_LINES)
            glVertex2f(x,0)
            glVertex2f(x,20)
            glEnd()

        glColor3f(0.5, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(0, 20)
        glEnd()

        glColor3f(0.0, 0.5, 0.0)
        glBegin(GL_LINES)
        glVertex2f(20, 0)
        glVertex2f(20, 20)
        glEnd()

    @staticmethod
    def _draw_hollow_circle(pos, radius):
        glBegin(GL_LINE_LOOP)

        for i in range(cfg.GRAPHICS_CIRCLE_VERTICES):
            theta = (2 * np.pi * i) / cfg.GRAPHICS_CIRCLE_VERTICES
            glVertex2f(
                (np.cos(theta) * radius + pos[0]),
                (np.sin(theta) * radius + pos[1])
            )

        glEnd()

    @staticmethod
    def _draw_hollow_square(pos, heading, diagonal):
        glBegin(GL_LINE_LOOP)
        # front right
        glVertex2f(
            pos[0] + (np.cos(heading - (cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading - (cfg.PI / 4)) * diagonal)
        )
        # back right
        glVertex2f(
            pos[0] + (np.cos(heading - (3 * cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading - (3 * cfg.PI / 4)) * diagonal)
        )
        # back left
        glVertex2f(
            pos[0] + (np.cos(heading + (3 * cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading + (3 * cfg.PI / 4)) * diagonal)
        )
        # front left
        glVertex2f(
            pos[0] + (np.cos(heading + (cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading + (cfg.PI / 4)) * diagonal)
        )
        glEnd()


# Note: Message Based Display, Still needs to be inplemented
#
# Note: there should be a more general Display
#   Sim_Display and Env_Display are children of display
#
# Note: to stay general Display should have a subject (self.subject
#   Display is the medium
#   Robots are the paint
#   Subject decides where to put what

class Sim_Display(pyglet.window.Window):

    def __init__(self, Sim_Node, timescale=1.0, self_update=True):
        super(Sim_Display, self).__init__(700,700)

        self._timescale = timescale
        self.update_func = (lambda a,b:0)
        self._click_callback = (lambda a,b:None)
        self._paused = False
        self._elapsed = 0.0
        self.delta = None

        if self_update:
            pyglet.clock.schedule_interval(self._update, 1.0/self._timescale/60.0)
            pyglet.clock.set_fps_limit(self._timescale*60)

        self.start_time = time.time()

        self.subject = Sim_Node
        self.roombaList_msg = None

    def set_click_callback(self, callback):
        self._click_callback = callback

    def _update(self, dt):
        if not self._paused:
            self.subject.roomba_topic = self.subject.get_roomba_data()
            self.delta = self.subject.get_delta()

    def on_resize(self, width, height):
        glViewport(10, 10, width-20, height-20)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 20, 0, 20, -1, 1)

        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glEnable( GL_BLEND );

# BEGIN EDIT

    def on_draw(self):

        pyglet.clock.tick()

        glClear(GL_COLOR_BUFFER_BIT)
        
        Sim_Display._draw_gridlines()

        self._draw_header(self.subject.headerArgs,
                          self.subject.headerLabels)

        roombaListDiff = self.subject.get_diff_msg()
    
        roombaListProbTR, roombaListProbOR = self.subject.get_prob_msgs()

        if not len(roombaListDiff) == 0:

            for roomba in roombaListDiff:

                XYR = (roomba.x, roomba.y, 0.22)

                Sim_Display._draw_probability_radius(XYR)

        if not len(roombaListProbTR) == 0:

            for roomba in roombaListProbTR:

                XYR = (roomba.x, roomba.y, roomba.prob_rad)
                
                Sim_Display._draw_probability_radius(XYR)
                
        if not len(roombaListProbOR) == 0:
            
            for roomba in roombaListProbOR:

                XYR = (roomba.x, roomba.y, 0.22)

                Sim_Display._draw_obstacle_roomba(XYR)

        Sim_Display._draw_drone(self.subject.agent)

	'''
        pyglet.clock.tick()
        glClear(GL_COLOR_BUFFER_BIT)

        Sim_Display._draw_gridlines()

        self._draw_header(self.subject.headerArgs,
                          self.subject.headerLabels)

        if (len(self.subject.roomba_topic.roombaList) == 0):
            print('msg empty')
            return

        for roomba in self.subject.roomba_topic.roombaList:
            if not roomba.detected:
                XYR = self.get_XYR(roomba)
                Sim_Display._draw_probability_radius(roomba, XYR, self.delta)
                continue

            if roomba.id < 9:
                XYR = self.get_XYR(roomba)
                Sim_Display._draw_probability_radius(roomba, XYR, self.delta)
            else:
                Sim_Display._draw_obstacle_roomba(roomba)

        Sim_Display._draw_drone(self.subject.agent)
	'''

    def on_mouse_release(self, x, y, button, modifiers):

        x = (x - 10) * 20.0 / (self.get_size()[0] - 20.0)
        y = (y - 10) * 20.0 / (self.get_size()[1] - 20.0)

        if self.roombaList_msg == None:
            return

        for roomba in self.roombaList_msg:
            if roomba.id < 9:
                if np.hypot(x - roomba.x, y - roomba.y) < cfg.ROOMBA_RADIUS:
                    self._click_callback(r,
                                         'left'
                                         if button == pyglet.window.mouse.LEFT
                                         else 'right')
                    break
        else:
            self._click_callback((x, y),
                                 'left'
                                 if button == pyglet.window.mouse.LEFT
                                 else 'right')

    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self._paused = not self._paused

    def get_XYR(self, roomba):
        return self.subject.XYR[roomba.id - 1]
		
	'''
    @staticmethod
    def _draw_probability_radius(r, XYR, delta):
        print(XYR)
        #vertex_count = cfg.GRAPHICS_CIRCLE_VERTICES
        if (XYR[0] != 0 and XYR[1] != 0):
            if( XYR[2] >= cfg.ROOMBA_MAX_RADIUS):
                XYR = (0,0,0)
            else:
                radius = XYR[2] + cfg.ROOMBA_LINEAR_SPEED * delta
                Sim_Display._draw_hollow_circle((XYR[0],XYR[1]),radius)
	'''
    @staticmethod
    def _draw_probability_radius(XYR):

	   Sim_Display._draw_hollow_circle((XYR[0],XYR[1]), XYR[2])


    @staticmethod
    def _draw_target_roomba(r, special_state=None):
        pos = (r.x, r.y)
        #heading = r.heading
        vertex_count = cfg.GRAPHICS_CIRCLE_VERTICES
        radius = cfg.ROOMBA_RADIUS

        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

        # Outline
        # if special_state == 'hitting':
        #     glColor3f(0.7, 0.7, 1.0)
        # elif special_state == 'blocking':
        #     glColor3f(0.7, 1.0, 0.7)
        # elif r.state == cfg.ROOMBA_STATE_FORWARD:
        #     glColor3f(1,1,1)
        # elif r.state in (cfg.ROOMBA_STATE_TURNING_NOISE,
        #                  cfg.ROOMBA_STATE_REVERSING,
        #                  cfg.ROOMBA_STATE_TOUCHED):
        #     glColor3f(1,0.8,0.8)

        Sim_Display._draw_hollow_circle(pos, radius)

        # Direction indicator
        glBegin(GL_LINES)

        glVertex2f(pos[0], pos[1])
        #glVertex2f(np.cos(heading) * radius + pos[0], np.sin(heading) * radius + pos[1])

        glEnd()

	'''
    @staticmethod
    def _draw_obstacle_roomba(r):
        pos = (r.x, r.y)
        #heading = r.heading
        vertex_count = cfg.GRAPHICS_CIRCLE_VERTICES
        radius = cfg.ROOMBA_RADIUS

        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

        # Outline
        # if r.state == cfg.ROOMBA_STATE_FORWARD or True:
        #     glColor3f(1,0.2,0.2)
        # elif r.state == cfg.ROOMBA_STATE_TURNING:
        #     glColor3f(1,0.8,0.8)

        Sim_Display._draw_hollow_circle(pos, radius)

        # Direction indicator
        glBegin(GL_LINES)

        glVertex2f(pos[0], pos[1])
        # glVertex2f(np.cos(heading) * radius + pos[0], np.sin(heading) * radius + pos[1])

        glEnd()
	'''

    @staticmethod
    def _draw_obstacle_roomba(pos):
        #heading = r.heading
        vertex_count = cfg.GRAPHICS_CIRCLE_VERTICES
        radius = cfg.ROOMBA_RADIUS

        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

        # Outline
        # if r.state == cfg.ROOMBA_STATE_FORWARD or True:
        #     glColor3f(1,0.2,0.2)
        # elif r.state == cfg.ROOMBA_STATE_TURNING:
        #     glColor3f(1,0.8,0.8)

        Sim_Display._draw_hollow_circle(pos, 0.2)

        # Direction indicator
        glBegin(GL_LINES)

        glVertex2f(pos[0], pos[1])
        # glVertex2f(np.cos(heading) * radius + pos[0], np.sin(heading) * radius + pos[1])

        glEnd()

    @staticmethod
    def _draw_drone(drone=None):
        if cfg.RENDER_AGENT != None:
            cfg.RENDER_AGENT(drone)
        else:
            cfg.RENDER_AGENT()

    def _draw_header(self, values, labels):
        # mins = elapsed_secs // 60
        # secs = elapsed_secs % 60
        self.set_caption(
            '%s %d %s %d %s %d %s %d'%(
                labels[0],
                values[0],
                labels[1],
                values[1],
                labels[2],
                values[2],
                labels[3],
                values[3]))

    @staticmethod
    def _draw_gridlines():

        # draw horizontal lines
        for y in range(0,21):
            if y % 5 == 0:
                glColor3f(0.5,0.5,0.5)
            else:
                glColor3f(0.25,0.25,0.25)

            glBegin(GL_LINES)
            glVertex2f(0,y)
            glVertex2f(20,y)
            glEnd()

        # draw vertical lines
        for x in range(1,20):
            if x % 5 == 0:
                glColor3f(0.5,0.5,0.5)
            else:
                glColor3f(0.25,0.25,0.25)

            glBegin(GL_LINES)
            glVertex2f(x,0)
            glVertex2f(x,20)
            glEnd()

        glColor3f(0.5, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(0, 20)
        glEnd()

        glColor3f(0.0, 0.5, 0.0)
        glBegin(GL_LINES)
        glVertex2f(20, 0)
        glVertex2f(20, 20)
        glEnd()

    @staticmethod
    def _draw_hollow_circle(pos, radius):
        glBegin(GL_LINE_LOOP)

        for i in range(cfg.GRAPHICS_CIRCLE_VERTICES):
            theta = (2 * np.pi * i) / cfg.GRAPHICS_CIRCLE_VERTICES
            glVertex2f(
                (np.cos(theta) * radius + pos[0]),
                (np.sin(theta) * radius + pos[1])
            )

        glEnd()

    @staticmethod
    def _draw_hollow_square(pos, heading, diagonal):
        glBegin(GL_LINE_LOOP)
        # front right
        glVertex2f(
            pos[0] + (np.cos(heading - (cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading - (cfg.PI / 4)) * diagonal)
        )
        # back right
        glVertex2f(
            pos[0] + (np.cos(heading - (3 * cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading - (3 * cfg.PI / 4)) * diagonal)
        )
        # back left
        glVertex2f(
            pos[0] + (np.cos(heading + (3 * cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading + (3 * cfg.PI / 4)) * diagonal)
        )
        # front left
        glVertex2f(
            pos[0] + (np.cos(heading + (cfg.PI / 4)) * diagonal),
            pos[1] + (np.sin(heading + (cfg.PI / 4)) * diagonal)
        )
        glEnd()
