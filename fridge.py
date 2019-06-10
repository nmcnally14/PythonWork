"""Demonstrate raiding a fridge"""

from contextlib import closing

class FridgeRaider:
    """Raid a fridge"""

    def open(self):
        print("Open fridge door")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health Warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")

def raid(food):
    with closing(FridgeRaider()) as r:
        r.open()
        r.take(food)
