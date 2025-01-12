

class Player:
    color = (255,255,0)

    def __init__(self, pos=(1.5, 1.5), drill_level=1, speed_level=1, forge_level=1, money=0):
        self.pos = list(pos)
        self.drill_level = drill_level
        self.speed_level = speed_level
        self.forge_level = forge_level
        self.money = money

    def mining_speed(self):
        return 10 * self.drill_level

    def luck_factor(self):
        return self.forge_level

    def movement_speed(self):
        return 0.05 * self.speed_level

    def move(self, world, control):
        move = self.dir_from_control(control)
        move = [move[0] * self.movement_speed(), move[1] * self.movement_speed()]
        coll, move = self.collision(world, move)
        self.pos[0] += move[0]
        self.pos[1] += move[1]
        if coll is not None:
            self.mine(world, coll)

    def collision(self, world, move):
        new_move = list(move)
        coll = None
        barr = False

        if move[0] > 0:
            corner1 = int(self.pos[0] + move[0] + .3), int(self.pos[1] + .3)
            corner2 = int(self.pos[0] + move[0] + .3), int(self.pos[1] - .3)
            if corner1[0] >= world.size:
                barr = True
                new_move[0] = corner1[0] - .31 - self.pos[0]
            elif world.content[int(self.pos[1])][corner1[0]] is not None:
                coll = corner1[0], int(self.pos[1])
                new_move[0] = coll[0] - .31 - self.pos[0]
            elif world.content[corner1[1]][corner1[0]] is not None:
                coll = corner1
                new_move[0] = coll[0] - .31 - self.pos[0]
            elif world.content[corner2[1]][corner2[0]] is not None:
                coll = corner2
                new_move[0] = coll[0] - .31 - self.pos[0]
        elif move[0] < 0:
            corner3 = int(self.pos[0] + move[0] - .3), int(self.pos[1] + .3)
            corner4 = int(self.pos[0] + move[0] - .3), int(self.pos[1] - .3)
            if self.pos[0] + move[0] - .3 < 0:
                barr = True
                new_move[0] = corner3[0] + .31 - self.pos[0]
            elif world.content[int(self.pos[1])][corner3[0]] is not None:
                coll = corner3[0], int(self.pos[1])
                new_move[0] = coll[0] + 1 + .31 - self.pos[0]
            elif world.content[corner3[1]][corner3[0]] is not None:
                coll = corner3
                new_move[0] = coll[0] + 1 + .31 - self.pos[0]
            elif world.content[corner4[1]][corner4[0]] is not None:
                coll = corner4
                new_move[0] = coll[0] + 1 + .31 - self.pos[0]
        if move[1] > 0:
            corner1 = int(self.pos[0] + .3), int(self.pos[1] + move[1] + .3)
            corner3 = int(self.pos[0] - .3), int(self.pos[1] + move[1] + .3)
            if corner1[1] >= world.size:
                barr = True
                new_move[1] = corner1[1] - .31 - self.pos[1]
            elif world.content[corner1[1]][int(self.pos[0])] is not None:
                coll = int(self.pos[0]), corner1[1]
                new_move[1] = coll[1] - .31 - self.pos[1]
            elif world.content[corner1[1]][corner1[0]] is not None:
                coll = corner1
                new_move[1] = coll[1] - .31 - self.pos[1]
            elif world.content[corner3[1]][corner3[0]] is not None:
                coll = corner3
                new_move[1] = coll[1] - .31 - self.pos[1]
        elif move[1] < 0:
            corner2 = int(self.pos[0] + .3), int(self.pos[1] + move[1] - .3)
            corner4 = int(self.pos[0] - .3), int(self.pos[1] + move[1] - .3)
            if self.pos[1] + move[1] - .3 < 0:
                barr = True
                new_move[1] = corner2[1] + .31 - self.pos[1]
            elif world.content[corner2[1]][int(self.pos[0])] is not None:
                coll = int(self.pos[0]), corner2[1]
                new_move[1] = coll[1] + 1 + .31 - self.pos[1]
            elif world.content[corner2[1]][corner2[0]] is not None:
                coll = corner2
                new_move[1] = coll[1] + 1 + .31 - self.pos[1]
            elif world.content[corner4[1]][corner4[0]] is not None:
                coll = corner4
                new_move[1] = coll[1] + 1 + .31 - self.pos[1]

        if coll is None and not barr and move[0] != 0 and move[1] != 0:
            corner = (int(self.pos[0] + move[0] + (.3 if move[0] > 0 else -.3)),
                      int(self.pos[1] + move[1] + (.3 if move[1] > 0 else -.3)))
            if world.content[corner[1]][corner[0]] is not None:
                coll = corner
                new_move[0] = coll[0] + (-.31 if move[0] > 0 else 1.31) - self.pos[0]
                new_move[1] = coll[1] + (-.31 if move[1] > 0 else 1.31) - self.pos[1]

        return coll, new_move

    @staticmethod
    def dir_from_control(control):
        move = [0, 0]
        if control[0] ^ control[1]:
            move[1] = 1 if control[1] else -1
        if control[2] ^ control[3]:
            move[0] = 1 if control[3] else -1
        if move[0] != 0 and move[1] != 0:
            move[0] /= 1.4
            move[1] /= 1.4
        return move

    def mine(self, world, coll):
        block = world.content[coll[1]][coll[0]]
        block.health -= self.mining_speed()
        if block.health <= 0:
            self.money += int(self.luck_factor() * block.value())
            world.content[coll[1]][coll[0]] = None
