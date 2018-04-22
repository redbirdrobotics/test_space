from real_game.redbird import Corvus, render

import numpy as np

#
# IMPLEMENTATION SPECIFIC CONSTANTS
#
AGENT = Corvus

DRONE_MAX_VERTICAL_VELOCITY = 1.0
DRONE_MAX_HORIZ_ACCEL = 3.0
DRONE_MAX_HORIZ_VELOCITY = 3.0


RENDER_AGENT = render.render_corvus

#
# REDBIRD DRONE CONFIGURATION
#

# the radius of sight for drone
CORVUS_FOV = 3

# the width of the square bumper base in meters
CORVUS_BASE_WIDTH = 0.57

# the distance from the center to a corner in meters
CORVUS_BASE_DIAGONAL = (CORVUS_BASE_WIDTH / 2) * np.sqrt(2)

# the radius of the roomba bumper pad im meters
CORVUS_PAD_RADIUS = 0.175

# altitude of the drone that will cause contact
# with the roombas
CORVUS_PAD_ACTIVIATION_HEIGHT = 0.03

# radius of outer edge of prop guards in meters
CORVUS_PROP_RADIUS = 0.155

# velocity with which to take off with
REDBIRD_TAKEOFF_VELOCITY = 0.3

# height at which to consider takeoff finished in meters
# should be higher than min_maneuver_height
REDBIRD_TAKEOFF_COMPLETE_HEIGHT = 0.7

# delay between arming and taking off
REDBIRD_DELAY_BEFORE_TAKEOFF = 0.0

# altitude when we transition from acro to angle mode
REDBIRD_TAKEOFF_ANGLE_MODE_HEIGHT = 0.2

# timeout for transforms
REDBIRD_TAKEOFF_TRANSFORM_TIMEOUT = 0.2

# velocity with which to land with
REDBIRD_LAND_VELOCITY = -0.2

# distance from the target that the XYZTranslationTask
# will deem "close enough" in meters
REDBIRD_XYZ_TRANSLATION_ACCURACY = 0.2

# PID constants for xy controller
# [Kp,Kd,Ki]
REDBIRD_PID_XY = np.array([0.5, 1.1, 0])

# PID constants for z controller
# [Kp,Kd,Ki]
REDBIRD_PID_Z = np.array([0.9, 0, 0])

# PID constants for yaw controller
# [Kp,Kd,Ki]
REDBIRD_PID_YAW = np.array([0.5, 0, 0])

# hover height while tracking roomba in meters
REDBIRD_TRACK_ROOMBA_HEIGHT = 1

# minimum distance to allow hit roomba task to run in meters
REDBIRD_HIT_ROOMBA_MAX_START_DIST = 0.5

# descent velocity for hit roomba task
REDBIRD_HIT_DESCENT_VELOCITY = -0.2

REDBIRD_BLOCK_DESCENT_VEL = -0.4
REDBIRD_BLOCK_FLOOR_TIME = 1.5
REDBIRD_HIT_ROOMBA_DESCENT_VELOCITY = -0.4
REDBIRD_HIT_ROOMBA_FLOOR_TIME = 0.2

# Tolerance for distance comparasion in the HoldPositionTask
REDBIRD_HOLD_POSITION_TOLERANCE = 0.2

# Tolerance for speed comparasion in the VelocityTask
REDBIRD_VELOCITY_TOLERANCE = 0.1