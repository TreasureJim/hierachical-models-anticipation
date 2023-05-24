#!/sbin/python

"""
Meant to represent a warehouse with automated forklifts and a single dropoff point
Only one forklift can occupy a "zone" at a time
"""

import simpy
import random
import zone, car, container
import simulation


env = simpy.Environment()
# Get same output each time
random.seed(0)

# Setup 
simulation.pickup = zone.OneCarZone(env)
simulation.dropoff = zone.OneCarZone(env)

env.process(container.spawn_orders(env))

for i in range(4):
    container.create_order()
    env.process(car.car(env, i))


# Start simulation
env.run(until=100)
