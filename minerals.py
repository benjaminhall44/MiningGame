

class Mineral:
    def __init__(self, value, health, color):
        self.value = value
        self.health = health
        self.color = color


DIRT = Mineral(1, 200, (200, 100, 0))
CLAY = Mineral(2, 400, (150, 125, 100))

SANDSTONE = Mineral(2, 400, (200, 150, 50))
COAL = Mineral(3, 800, (0, 0, 0))

LIMESTONE = Mineral(3, 600, (220, 220, 150))
LEAD = Mineral(5, 1200, (20, 0, 100))

SHALE = Mineral(4, 800, (100, 60, 25))
IRON = Mineral(8, 1600, (120, 100, 100))

BASALT = Mineral(5, 1000, (50, 50, 50))
COPPER = Mineral(12, 2000, (255, 128, 0))

GRANITE = Mineral(6, 1200, (200, 100, 100))
SILVER = Mineral(17, 2400, (230, 230, 240))

OBSIDIAN = Mineral(7, 1400, (100, 0, 100))
GOLD = Mineral(23, 2800, (255, 255, 0))

MARBLE = Mineral(8, 1600, (240, 240, 240))
SAPPHIRE = Mineral(30, 3200, (0, 0, 255))

SLATE = Mineral(9, 1800, (100, 100, 100))
RUBY = Mineral(38, 3600, (255, 0, 0))

SCHIST = Mineral(10, 2000, (180, 200, 200))
EMERALD = Mineral(47, 4000, (0, 255, 0))

KIMBERLITE = Mineral(11, 2200, (100, 150, 100))
DIAMOND = Mineral(57, 4400, (230, 230, 255))

MAGMA = Mineral(12, 2400, (250, 150, 0))
TITANIUM = Mineral(68, 4800, (200, 0, 200))

MITHRIL = Mineral(80, 5200, (200, 200, 255))
