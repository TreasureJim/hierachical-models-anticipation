import simpy
import random
from collections import deque
import simulation

class Container:
    def __init__(self, id, active) -> None:
        self.id = id
        self.dest = None
        self.active = active

    def complete_order(self):
        self.dest = None
        self.active = True


delivery_orders = deque()
containers = [None] * 30

# initialize containers
for i in range(len(containers)):
    containers[i] = Container(i, bool(random.getrandbits(1)))

def create_order():
    # Select random crate to make order for that doesn't already have a destination
    target = random.choice(list(filter(lambda c: c.dest == None, containers)))

    #if on the shelves already send to dropoff
    if (target.active):
        target.dest = simulation.dropoff
    #not on shelves yet so retrieve from pickup area
    else:
        target.dest = simulation.pickup

    target.active = False
    delivery_orders.append(target)

def spawn_orders(env):
    while(True):
        create_order()
        yield env.timeout(3)

def get_order():
    return delivery_orders.popleft()