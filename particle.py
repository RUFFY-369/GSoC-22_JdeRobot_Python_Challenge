#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


MAX_SPEED = 10


# minimum distance between particle and container
MIN_DIST = 2

X_LIMITS = (75, 525)
Y_LIMITS = (75, 525)



class Particle:
    def __init__(self, vel, position, r, mass,
                 color):
        self.vel = vel
        self.pos = position  
        self.r = r  #radius
        self.mass = mass
        self.color = color

    def update_position(self, other_particles) -> None:
        
        # checking for collision with wall and update velocity 
        self.check_wall_collision()

        # constrain new velocity of particle from making it go beyond a wall container in the next frame
        self.check_go_past_wall()

        # update position with updated velocity
        self.pos = np.array(
            [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]
        )

    def get_position(self) :
        return self.pos[0], self.pos[1]


    def check_wall_collision(self) -> bool:
        """For checking if the particle has collided with any of the arena walls
        and update the particle's velocity for performing elastic collision if so.

        Condition for collision: particle being within 2 pixels of a wall,
        including the radius of the particle.
        """
        # check for collision with left/right container borders
        # condition for collision: particle is MIN_DIST + radius units away from arena's border
        del_left = self.pos[0] - (X_LIMITS[0] + MIN_DIST + self.r)
        del_right = (X_LIMITS[1] - MIN_DIST - self.r) - self.pos[0]
        del_top = self.pos[1] - (Y_LIMITS[0] + MIN_DIST + self.r)
        del_bottom = (Y_LIMITS[1] - MIN_DIST - self.r) - self.pos[1]
        # collision with left or right side of arena
        if del_left <=0 or del_right <= 0:
      
            if np.dot(self.vel, np.array([0, 1])) == 0:
                self.vel = -self.vel
            else:
               
                self.vel = np.array([self.vel[1], -self.vel[0]])
            
        elif del_top <= 0 or del_bottom <= 0:
            # particle velocity perpendicular to top/bottom border
            if np.dot(self.vel, np.array([1, 0])) == 0:
                self.vel = -self.vel
            else:
                self.vel = np.array([self.vel[1], -self.vel[0]])
            
    
    def check_go_past_wall(self) -> None:
        """For constraining new velocity of particle from making it go beyond a wall container in the next frame
        Make the particle "collide" with the wall it is about to pass if so
        """
        future_x = self.pos[0] + self.vel[0]
        future_y = self.pos[1] + self.vel[1]

        del_left_future = future_x - (X_LIMITS[0] + MIN_DIST + self.r)
        del_right_future = (X_LIMITS[1] - MIN_DIST - self.r) - future_x
        del_top_future = future_y - (Y_LIMITS[0] + MIN_DIST + self.r)
        del_bottom_future = (Y_LIMITS[1] - MIN_DIST - self.r) - future_y

        if del_left_future <= 0 or del_right_future <= 0:
            # particle's velocity is perpendicular to left/right border, so
           
            if np.dot(self.vel, np.array([0, 1])) == 0:
                self.vel = np.array([-self.vel[0], np.random.uniform(low = -MAX_SPEED, high = MAX_SPEED,
                                         size = (2,))[0]])
                
            else:
                
                self.vel = np.array([self.vel[1], np.random.uniform(low = -MAX_SPEED, high = MAX_SPEED,
                                         size = (2,))[0]])
            print("Collision to left/right border")

        elif del_top_future <= 0 or del_bottom_future <= 0:
            # particle velocity perpendicular to top/bottom border
            if np.dot(self.vel, np.array([1, 0])) == 0:
                self.vel = np.array([np.random.uniform(low = -MAX_SPEED, high = MAX_SPEED,
                                         size = (2,))[0],-self.vel[1]]) 
            else:
                self.vel = np.array([np.random.uniform(low = -MAX_SPEED, high = MAX_SPEED,
                                         size = (2,))[0], -self.vel[0]])
            print("Collision to top/bottom border")
