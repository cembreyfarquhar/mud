import random


# Attributes
# health
# strength
# luck

class Player:
    def __init__(self):
 		total_attr_points = 20
        self.health = random.randint(0, total_attr_points)
        total_attr_points -= self.health
        self.strength = random.randint(0, total_attr_points)
        total_attr_points -= self.strength
        self.luck = random.randint(0, total_attr_points)
