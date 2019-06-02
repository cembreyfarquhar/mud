import random
import math

# Attributes
# health
# strength
# luck


class Player:
    def __init__(self):
        total_attr_points = 20
        self.health = random.randint(2, math.floor(total_attr_points / 1.5))
        total_attr_points -= self.health
        self.strength = random.randint(2, math.floor(total_attr_points / 1.25))
        total_attr_points -= self.strength
        self.luck = random.randint(2, total_attr_points)

    def get_stats(self, stat='all'):
        switcher = {
            'all': [self.health, self.strength, self.luck],
            'health': self.health,
            'strength': self.strength,
            'luck': self.luck
        }
        return switcher.get(stat, 'Invalid attribute')
