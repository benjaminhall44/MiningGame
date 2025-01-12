import random
from block import Block


class World:
    def __init__(self, size, tier, regen):
        self.size = size
        self.tier = tier
        self.regen = regen
        self.content: list[list[Block|None]] = [[Block(tier) for _ in range(size)] for _ in range(size)]
        self.content[size // 2][size // 2] = None

    def update(self, player):
        for i in range(self.size):
            for j in range(self.size):
                if ((int(player.pos[0] - .3) == i or int(player.pos[0] + .3) == i) and
                        (int(player.pos[1] - .3) == j or int(player.pos[1] + .3) == j)):
                    continue
                elif self.content[j][i] is None:
                    if random.randint(0, 2048) < self.regen:
                        self.content[j][i] = Block(self.tier)
