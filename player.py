import random
import math

# Attributes
# health
# strength
# luck


class Player:
    def __init__(self):
        self.stats = {}
        total_attr_points = 20
        self.stats['health'] = random.randint(
            2, math.floor(total_attr_points / 1.5))
        self.stats['strength'] = random.randint(
            2, math.floor(total_attr_points / 1.25))
        self.stats['luck'] = random.randint(
            2, math.floor(total_attr_points))
