'''
config.py

Contains a bunch of modifiable constants organized by
module type.
'''
#from real_game.redbird import Corvus

import re
import numpy as np

_const_rgx = re.compile('(([A-Z_][A-Z0-9_]*)|(__.*__))$')
 
def load(module):
    '''
    Copies all module-level constants from `module`
    into this module.

    Identifiers must match _const_rgx and can't start
    with '_' in order to be copied.
    '''
    # slightly hacky
    g = globals()
    for attr in dir(module):
        if not attr.startswith('_') and _const_rgx.match(attr):
            g[attr] = getattr(module, attr)


#
# IMPLEMENTATION SPECIFIC CONSTANTS
# define these in a separate file and use cfg.load(module)
#

# Should point to a subclass of agent.drone
# Defines the agent to initialize in the environment
AGENT = None

DRONE_MAX_VERTICAL_VELOCITY = float('Inf')
DRONE_MAX_HORIZ_ACCEL = float('Inf')
DRONE_MAX_HORIZ_VELOCITY = float('Inf')

# (optional)
# Defines a method to render the agent in the opengl
# context. See roombasim.graphics.display for examples.
RENDER_AGENT = None

#
# MATH CONSTANTS
#

# please don't change these ;p
PI = np.pi
TAU = np.pi * 2

#
# ROOMBA CONFIGURATION
#

# Speed of the roomba moving forwards
ROOMBA_LINEAR_SPEED = 0.33 # m/s

# Turning speed of the roomba
ROOMBA_ANGULAR_SPEED = 1.279 # rad/s

# Time until a full reverse (milliseconds)
ROOMBA_REVERSE_PERIOD = 20000

# Time until random heading noise is applied (milliseconds)
ROOMBA_HEADING_NOISE_PERIOD = 5000

# Maximum heading noise (applied in either direction) in radians
ROOMBA_HEADING_NOISE_MAX = 20 * (np.pi / 180)

# Time spent doing noisy turns (milliseconds)
ROOMBA_NOISE_DURATION = 850

# Python doesn't have enums...
ROOMBA_STATE_IDLE = 0
ROOMBA_STATE_FORWARD = 1
ROOMBA_STATE_TOUCHED = 2
ROOMBA_STATE_REVERSING = 3
ROOMBA_STATE_TURNING_NOISE = 4

# Roomba's radius in meters
ROOMBA_RADIUS = 0.35 / 2

#
# MISSION CONFIGURATION
#

# number of target roombas to spawn
MISSION_NUM_TARGETS = 10

# radius to spawn target roombas (centered at origin) in meters
MISSION_TARGET_SPAWN_RADIUS = 1

# number of obstacle roombas to spawn
MISSION_NUM_OBSTACLES = 4

# radius to spawn obstacle roombas in meters
MISSION_OBSTACLE_SPAWN_RADIUS = 5

#
# GRAPHICS CONFIGURATION
#

# how many vertices to use to draw circles
# (note: hopefully someone can implement fragment shaders
# and this will become irrelevant)
GRAPHICS_CIRCLE_VERTICES = 10

AGENT = None

DRONE_MAX_VERTICAL_VELOCITY = 1.0
DRONE_MAX_HORIZ_ACCEL = 3.0
DRONE_MAX_HORIZ_VELOCITY = 3.0

# CONTROLLER = WaypointDemoController

# TASKS = {
#     'HoldPositionTask': HoldPositionTask,
#     'XYZTranslationTask': XYZTranslationTask,
#     'TakeoffTask': TakeoffTask,
#     'GoToRoombaTask': GoToRoombaTask,
#     'TrackRoombaTask': TrackRoombaTask,
#     'HitRoombaTask': HitRoombaTask,
#     'LandTask': LandTask,
#     'BlockRoombaTask': BlockRoombaTask,
#     'VelocityTask': VelocityTask
# }

# STATES = {
#     'DroneState': DroneState,
#     'RoombaState': RoombaState
# }
