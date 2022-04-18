#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pygame
from particle_collection import ParticleCollection

pygame.init()

################################################################################


# Defining game window
WIDTH = 600
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Brownian Motion (GSoC'22 JdeRobot Python Challenge)")  # window name


# Simulation constants
MAX_PARTICLES = 2 # Number of particles -1
FPS = 75


def draw_window(manager: ParticleCollection) -> None:
    # filling background as white
    WINDOW.fill((255, 255, 255))

    # creating particle arena
    pygame.draw.rect(WINDOW,
                    (0, 0, 0),
                    (75, 75, 450, 450),
                     2)

 
    # updating particle velocities and positions
    manager.update_particles()

    # updating positions and colors of particle
    new_particle_info = manager.get_updated_particle_info()
    pygame.draw.circle(WINDOW, new_particle_info[0], new_particle_info[1], new_particle_info[2])

    # refreshing the display
    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()
    manager = ParticleCollection()

    #simulating particle for brownian motion
    manager.simulate_particles(np.random.randint(1, MAX_PARTICLES))
    
    while run:
        clock.tick(FPS)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window(manager)


if __name__ == '__main__':
    main()
