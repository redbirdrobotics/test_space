import numpy as np
from real_game.robots import Drone
import real_game.config as cfg
from real_game import geometry

class Corvus(Drone):

    def update(self, delta, elapsed):
        super(Corvus, self).update(delta, elapsed)

    def detects_roomba(self, rba):
        dist2 = pow((self.xy_pos[0] - rba.pos[0]), 2) + pow((self.xy_pos[1] - rba.pos[1]), 2)
        dist = np.sqrt(dist2)
        return dist < cfg.CORVUS_FOV

    def is_touching_roomba_top(self, rba):
        '''
        PittRAS drone pad has a diameter of 35cm.
        '''
        dist2 = pow((self.xy_pos[0] - rba.pos[0]), 2) + pow((self.xy_pos[1] - rba.pos[1]), 2)
        dist = np.sqrt(dist2)

        # If drone is close to floor and roomba is less than drone footprint return true else false
        return self.z_pos < cfg.CORVUS_PAD_ACTIVIATION_HEIGHT and dist < cfg.CORVUS_PAD_RADIUS

    def is_blocking_roomba(self, rba):
        '''
        PittRAS drone has a square base of width: 57cm
        '''
        hit_bumper = geometry.circle_intersects_square(rba.pos, cfg.ROOMBA_RADIUS, self.xy_pos, self.yaw, cfg.CORVUS_BASE_WIDTH)
        
        return hit_bumper and self.z_pos < cfg.CORVUS_PAD_ACTIVIATION_HEIGHT