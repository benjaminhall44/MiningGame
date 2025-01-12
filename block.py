import random

from mines import MINES


class Block:
    def __init__(self, tier):
        x = random.randint(0, 99)
        possible = MINES[tier].ores
        for mineral, chance in possible:
            x -= chance
            if x < 0:
                self.mineral = mineral
                break
        self.health = self.mineral.health

    def value(self):
        return self.mineral.value
