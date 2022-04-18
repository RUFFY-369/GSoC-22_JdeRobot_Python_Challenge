#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pygame
from particle_collection import ParticleCollection


class BrownianMotion():
    def __init__(self) -> None:
        pygame.init()

        # Defining game window
        self.WIDTH = 600
        self.HEIGHT = 600
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        pygame.display.set_caption("Brownian Motion (GSoC'22 JdeRobot Python Challenge)")  # window name


        # Simulation constants
        self.MAX_PARTICLES = 2 # Number of particles -1
        self.FPS = 75

    def draw_window(self,manager: ParticleCollection) -> None:
        # filling background as white
        self.WINDOW.fill((255, 255, 255))

        # creating particle arena
        pygame.draw.rect(self.WINDOW,
                        (0, 0, 0),
                        (75, 75, 450, 450),
                        2)

    
        # updating particle velocities and positions
        manager.update_particles()

        # updating positions and colors of particle
        new_particle_info = manager.get_updated_particle_info()
        pygame.draw.circle(self.WINDOW, new_particle_info[0], new_particle_info[1], new_particle_info[2])

        # refreshing the display
        pygame.display.update()



    def run_sim(self):
        run = True
        clock = pygame.time.Clock()
        manager = ParticleCollection()

        #simulating particle for brownian motion
        manager.simulate_particles(np.random.randint(1, self.MAX_PARTICLES))
        
        while run:
            clock.tick(self.FPS)  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            self.draw_window(manager)


