import simpy

class OneCarZone:
    def __init__(self, env):
        self.env = env
        self.location = simpy.Resource(env, capacity=1)
