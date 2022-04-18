#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from particle import Particle

# Constants for particle's physicality (Minimum and maximum speeds, masses and radii for simulated particle)
MIN_SPEED = 2
MAX_SPEED = 10
MIN_MASS = 12
MAX_MASS = 20
MIN_RADIUS = 12
MAX_RADIUS = 20

# Minimum and maximum values for both x and y coordinates of the particle, defined by the arena containing the particle
MIN_POS = 75 + 25
MAX_POS = 525 - 25

# initial default color of blue for particles
COLOR = (0, 0, 255)


################################################################################

class ParticleCollection:
    """Stores and collects simulated particle
    """
    def __init__(self):
        self.particle = None
        #Initial vel
        self.INIT_VELS = [[5.0,0.0],[-5.0,0.0],[0.0,5.0],[0.0,-5.0]]

    def simulate_particles(self, n) -> None:
        """Initialize the particle with random velocities in straight direction, positions, sizes and
        mass, storing the particles in self.particle.
        """
        for _ in range(n):
            rand_vel = np.array(self.INIT_VELS[np.random.randint(0,4)])
            init_pos = [300,300]
            rand_radius = np.random.randint(MIN_RADIUS, MAX_RADIUS)
            rand_mass = np.random.randint(MIN_MASS, MAX_MASS)

            self.particle = Particle(rand_vel, init_pos, rand_radius, rand_mass,
                                     COLOR)

        

    def update_particles(self) -> None:
        """For updating velocities and positions for particle in self.particle
        in a single frame, based on its velocities and collisions.
        """
        
        self.particle.update_position([self.particle])
        


    
    def get_updated_particle_info(self):
        """Return a tuple, containing the new color, position and radius for the particle.
        """
    
        new_col = (np.clip(30 * np.linalg.norm(self.particle.vel), 0, 255), 0, 255)
        new_pos = self.particle.get_position()
        r = self.particle.r

        particle_tuples = (new_col, new_pos, r)

        return particle_tuples
    
    

    
