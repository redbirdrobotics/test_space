
from pyglet.gl import *
import numpy as np

import config as cfg
from display import Env_Display
import geometry

def render_corvus(drone):
    glEnable(GL_BLEND)
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

    # altitude indicator
    # alpha is 1 when landed and 0 when >= 2 meters
    alpha = max(min(((-0.5 * drone.z_pos) + 1), 1), 0)
    glColor4f(0.5,0.5,0.5,alpha)

    scale = ((1 - alpha) * 3) + 1
    Env_Display._draw_hollow_square(drone.xy_pos, drone.yaw, cfg.CORVUS_BASE_DIAGONAL * scale)

    # draw bumpers
    if drone.z_pos <= cfg.CORVUS_PAD_ACTIVIATION_HEIGHT:
        glColor3f(1,0.5,0.5)
    else:
        glColor3f(1,1,1)
    Env_Display._draw_hollow_square(drone.xy_pos, drone.yaw, cfg.CORVUS_BASE_DIAGONAL)

    # draw prop guards
    glColor3f(0.8,0.8,0.5)
    for c in geometry.get_square_corners(drone.xy_pos, drone.yaw, cfg.CORVUS_BASE_WIDTH):
        Env_Display._draw_hollow_circle(c, cfg.CORVUS_PROP_RADIUS)

    # Direction indicator
    glColor3f(1,1,1)
    glBegin(GL_LINES)

    glVertex2f(drone.xy_pos[0], drone.xy_pos[1])
    glVertex2f(
        np.cos(drone.yaw) * (cfg.CORVUS_BASE_WIDTH / 2) + drone.xy_pos[0], 
        np.sin(drone.yaw) * (cfg.CORVUS_BASE_WIDTH / 2) + drone.xy_pos[1]
    )

    glEnd()

    '''
    # 2d velocity indicator
    glColor3f(0.5,1,0.5)
    glBegin(GL_LINES)

    glVertex2f(drone.xy_pos[0], drone.xy_pos[1])
    glVertex2f(
        drone.xy_pos[0] + drone.xy_vel[0], 
        drone.xy_pos[1] + drone.xy_vel[1]
    )

    glEnd()
    
    # 2d acceleration indicator
    glColor3f(0.5,0.5,1)
    glBegin(GL_LINES)

    glVertex2f(drone.xy_pos[0], drone.xy_pos[1])
    glVertex2f(
        drone.xy_pos[0] + drone._frame_accel[0], 
        drone.xy_pos[1] + drone._frame_accel[1]
    )

    glEnd()
    '''
