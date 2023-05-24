import random
import container

def car(env, car_id):
    while True:
        order = container.get_order()
        # distance is chosen randomly because this doesn't matter but in a real-life simulation would be calculated
        distance = random.randrange(5, 10)

        print(f"Car #{car_id} driving to package {order.id}")
        yield env.timeout(distance)
        print(f"Car #{car_id} delivering package {order.id}")
        yield env.timeout(distance)
        print(f"Car #{car_id} at order dest waiting...")

        assert order.dest != None, f"CAR #{car_id} PACKAGE {order.id} HAS NO DESTINATION"

        with order.dest.location.request() as location:
            yield location
            print(f"Car #{car_id} finishing order")
            order.complete_order()
            yield env.timeout(3)
