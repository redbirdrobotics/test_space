#!/usr/bin/env python

'''
 Title:         Demo Node

 Purpose:       Runs a demo of the ground and obstacle robots in a simulated
                environment. 
 Publisher:     
    Topic:      roomba_msgs ~ Contains data on all roombas
    Datatype:   roombaList_msg ~ An array of roomba_msg

'''
import time
import pyglet

import config as cfg
import redbird.redbird_config
from display import Env_Display
from environment import Environment
from communication import ROSExtension
from sim_game.msg import roomba_msg, roombaList_msg

__author__ = "Alex Rickert"


def main():    
    run_demo()

def run_demo():

    cfg.load(redbird.redbird_config)

    # Setup Environment
    environment = Environment()
    environment.make_node()
    environment.reset()

    # Setup agent
    agent = cfg.AGENT([13,10], 0)
    environment.agent = agent

    config = pyglet.gl.Config(sample_buffers=1, samples=4)

    # Setup Env_Display
    env_window = Env_Display(environment)

    def env_update_func(delta, elapsed):
        environment.update(delta, elapsed)

    env_window.set_update_func(env_update_func)

    # This function runs until esc pressed
    pyglet.app.run()

if __name__ == '__main__':
    main()
