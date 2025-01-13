import pygame
import json

from player import Player
from world import World
from mines import MINES
pygame.init()


class MiningGame:
    SCREEN_SIZE = (400, 400)

    def __init__(self, game_state):
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE, pygame.RESIZABLE)
        pygame.time.set_timer(pygame.USEREVENT, 50)

        self.world = World(game_state["width"], game_state["tier"], 10)
        self.player = Player((self.world.size / 2, self.world.size / 2),
                             game_state["drill_level"], game_state["speed_level"],
                             game_state["forge_level"], game_state["money"])
        self.playing = False

    def play(self):
        w_down = False
        s_down = False
        a_down = False
        d_down = False

        self.playing = True
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        w_down = True
                    elif event.key == pygame.K_s:
                        s_down = True
                    elif event.key == pygame.K_a:
                        a_down = True
                    elif event.key == pygame.K_d:
                        d_down = True
                    elif event.key == pygame.K_e:
                        self.upgrade_menu()
                        w_down = False
                        s_down = False
                        a_down = False
                        d_down = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        w_down = False
                    elif event.key == pygame.K_s:
                        s_down = False
                    elif event.key == pygame.K_a:
                        a_down = False
                    elif event.key == pygame.K_d:
                        d_down = False
                elif event.type == pygame.USEREVENT:
                    self.world.update(self.player)
                    self.player.move(self.world, (w_down, s_down, a_down, d_down))
                    self.animate()
                    pygame.display.flip()

    def animate(self):
        self.screen.fill((0, 0, 0))
        screen_size = self.screen.get_size()
        offset = [0, 0]
        side = min(screen_size)
        if screen_size[0] > screen_size[1]:
            offset = (screen_size[0] - screen_size[1]) // 2, 0
        elif screen_size[0] < screen_size[1]:
            offset = 0, (screen_size[1] - screen_size[0]) // 2
        block_size = side / self.world.size, side / self.world.size
        pygame.draw.rect(self.screen, MINES[self.world.tier].color, [offset[0], offset[1], side, side])
        x = offset[0]
        y = offset[1]
        for i in range(self.world.size):
            for j in range(self.world.size):
                block = self.world.content[i][j]
                if block is not None:
                    block_surface = pygame.Surface([int(x + block_size[0]) - int(x), int(y + block_size[1]) - int(y)], masks=(0, 0, 0, 0))
                    block_surface.fill(block.mineral.color)
                    block_surface.set_alpha(int(55.0 + 200.0 * block.health / block.mineral.health))
                    self.screen.blit(block_surface, [x-1, y-1])
                x += block_size[0]
            y += block_size[1]
            x = offset[0]
        pygame.draw.ellipse(self.screen, self.player.color,
                            [offset[0] + block_size[0] * (self.player.pos[0] - .4),
                             offset[1] + block_size[1] * (self.player.pos[1] - .4),
                             .8 * block_size[0],
                             .8 * block_size[1]])
        font = pygame.font.Font(pygame.font.get_default_font(), int(side * .1))
        self.screen.blit(font.render(f"${self.player.money}", 0, (0, 100, 0)),
                         [int(side * .02), int(side * .02)])

    def upgrade_menu(self):
        merch = self.generate_store()
        self.draw_upgrade_menu(merch)
        menu_open = True
        while menu_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_open = False
                    self.playing = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        menu_open = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = (event.pos[0] / self.screen.get_size()[0],
                               event.pos[1] / self.screen.get_size()[1])
                        row = int((pos[1] - .12) / .1)
                        if self.player.money >= merch[row][1]:
                            self.player.money -= merch[row][1]
                            if merch[row][0] == "Drill":
                                self.player.drill_level += 1
                            elif merch[row][0] == "Forge":
                                self.player.forge_level += 1
                            elif merch[row][0] == "Width":
                                self.world = World(self.world.size + 2, self.world.tier, self.world.regen)
                                self.player.pos = [self.world.size / 2, self.world.size / 2]
                            elif merch[row][0] == "Depth":
                                self.world = World(self.world.size, self.world.tier + 1, self.world.regen)
                                self.player.pos = [self.world.size / 2, self.world.size / 2]
                            elif merch[row][0] == "Speed":
                                self.player.speed_level += 1
                            merch = self.generate_store()
                            self.draw_upgrade_menu(merch)

    def generate_store(self):
        merch = []
        merch.append(("Drill", self.drill_upgrade_cost()))
        if self.player.speed_level < 5:
            merch.append(("Speed", self.speed_upgrade_cost()))
        if self.world.tier + 1 < len(MINES):
            merch.append(("Depth", self.tier_upgrade_cost()))
        merch.append(("Width", self.width_upgrade_cost()))
        merch.append(("Forge", self.luck_upgrade_cost()))
        return merch

    def draw_upgrade_menu(self, merch):
        self.animate()
        screen_size = self.screen.get_size()
        side = min(screen_size)
        font = pygame.font.Font(pygame.font.get_default_font(), int(side * .1))
        row = side * .12
        for item in merch:
            self.screen.blit(font.render(f"{item[0]} ${item[1]}", 0, (0, 100, 0)),
                             [int(side * .02), int(row)])
            row += side * .1
        pygame.display.flip()

    def drill_upgrade_cost(self):
        return int(10 * 2 ** (self.player.drill_level - 1))

    def speed_upgrade_cost(self):
        return int(25 * 2 ** (self.player.speed_level - 1))

    def tier_upgrade_cost(self):
        return int(50 * 2 ** self.world.tier)

    def width_upgrade_cost(self):
        return int(100 * 2 ** (self.world.size - 3))

    def luck_upgrade_cost(self):
        return int(200 * 4 ** (self.player.forge_level - 1))

    def save(self):
        return {
            "drill_level": self.player.drill_level,
            "speed_level": self.player.speed_level,
            "forge_level": self.player.forge_level,
            "money": self.player.money,
            "width": self.world.size,
            "tier": self.world.tier
        }


if __name__ == "__main__":
    try:
        file = open("save.json")
        data = json.load(file)
    except FileNotFoundError:
        data = {
            "drill_level": 1,
            "speed_level": 1,
            "forge_level": 1,
            "money": 0,
            "width": 3,
            "tier": 0
        }
    game = MiningGame(data)
    game.play()
    data = game.save()
    file = open("save.json", "w")
    json.dump(data, file, indent=2)
