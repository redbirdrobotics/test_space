#!/usr/bin/env python
'''
roombasim.py
CLI interface for various functions.
'''

#import argparse
import time
import pyglet

import real_game.config as cfg
from real_game.display import Display
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
    environment.reset()

    # setup agent
    agent = cfg.AGENT([13,10], 0)
    environment.agent = agent

    config = pyglet.gl.Config(sample_buffers=1, samples=4)
    # if args.timescale:
    #     window = Display(environment, args.timescale)
    # else:
    #     window = Display(environment)
    window = Display(environment)

    def update_func(delta, elapsed):
        environment.update(delta, elapsed)

    window.set_update_func(update_func)

    pyglet.app.run()

if __name__ == '__main__':
    main()
