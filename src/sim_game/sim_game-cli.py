#!/usr/bin/env python
'''
roombasim.py
CLI interface for various functions.
'''

#import argparse
import time
import pyglet

import real_game.config as cfg
from real_game.display import Env_Display, Sim_Display
from real_game.environment import Environment


def main():
        run_demo()

def run_demo():
    '''
    Runs a visual demo of roomba movement
    '''
    # if args.num_targets != None:
    #     cfg.MISSION_NUM_TARGETS = args.num_targets

    # if args.num_obstacles != None:
    #     cfg.MISSION_NUM_OBSTACLES = args.num_obstacles

    # if args.target_spawn_radius != None:
    #     cfg.MISSION_TARGET_SPAWN_RADIUS = args.target_spawn_radius

    # if args.obstacle_spawn_radius != None:
    #     cfg.MISSION_OBSTACLE_SPAWN_RADIUS = args.obstacle_spawn_radius


    import real_game.redbird.config
    cfg.load(real_game.redbird.config)

    # setup mission
    environment = Environment()
    environment.make_node()
    environment.reset()

    # setup agent
    agent = cfg.AGENT([13,10], 0)
    environment.agent = agent

    config = pyglet.gl.Config(sample_buffers=1, samples=4)

    # setup Env_Display
    env_window = Env_Display(environment)

    # setup Sim_Display
    #sim_window =Sim_Display(environment)

    def env_update_func(delta, elapsed):
        environment.update(delta, elapsed)

    env_window.set_update_func(env_update_func)
    #sim_window.set_update_func(sim_update_func)

    pyglet.app.run()

if __name__ == '__main__':
    main()
