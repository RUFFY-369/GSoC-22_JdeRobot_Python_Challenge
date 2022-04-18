#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import BrownianMotion

print("----------------------------------------------------------")
print("       	BEGIN THE SIMULATION FOR BROWNIAN MOTION         ")
print("----------------------------------------------------------")


print("Press Ctrl+C or close the Pygame window at any point to exit")
sim = BrownianMotion()
sim.run_sim()
	
print("------------SIMULATION ENDS---------------")
