#!/usr/bin/env python

'''
 Title:         Demo Node

 Purpose:       Runs a demo of the ground and obstacle robots in a simulated
                environment. 
 Publisher:     
    Topic:      roomba_msgs ~ Contains data on all roombas
    Datatype:   roombaList_msg ~ An array of roomba_msg

 Note:          This is based on the work done by Pittsburgh University's PittRAS team
'''
import time
import pyglet

import config as cfg
import redbird.redbird_config
from display import Sim_Display
from communication import ROSExtension
from onboard_simulation import Simulation_Node
from sim_game.msg import roomba_msg, roombaList_msg

__author__ = "Alex Rickert"


def main():    
    run_demo()

def run_demo():

    # Setup Simulation
    sim = Simulation_Node()
    sim.setup()

    config = pyglet.gl.Config(sample_buffers=1, samples=4)

    cfg.load(redbird.redbird_config)

    # Setup agent
    agent = cfg.AGENT([13,10], 0)
    sim.agent = agent

    # Setup Env_Display
    sim_window = Sim_Display(sim)

    # def sim_update_func(delta):
    #     sim.set_delta(delta)

    # This function runs until esc pressed
    pyglet.app.run()

if __name__ == '__main__':
    main()