from minerals import *


class Mine:
    def __init__(self, color, ores):
        self.color = color
        self.ores = ores
        if sum(a for _, a in self.ores) != 100:
            raise Exception(f"mine has incorrect ore list {color}, {ores}")


MINES = [
    Mine((220, 120, 50), ((DIRT, 100),)),
    Mine((220, 120, 50), ((DIRT, 75), (CLAY, 25))),
    Mine((220, 120, 50), ((DIRT, 75), (CLAY, 20), (COAL, 5))),
    Mine((220, 170, 70), ((SANDSTONE, 75), (COAL, 25))),
    Mine((220, 170, 70), ((SANDSTONE, 75), (COAL, 20), (LEAD, 5))),
    Mine((200, 200, 130), ((LIMESTONE, 75), (LEAD, 25))),
    Mine((200, 200, 130), ((LIMESTONE, 75), (LEAD, 20), (IRON, 5))),
    Mine((120, 80, 45), ((SHALE, 75), (IRON, 25))),
    Mine((120, 80, 45), ((SHALE, 75), (IRON, 20), (COPPER, 5))),
    Mine((70, 70, 70), ((BASALT, 75), (COPPER, 25))),
    Mine((70, 70, 70), ((BASALT, 75), (COPPER, 20), (SILVER, 5))),
    Mine((180, 80, 80), ((GRANITE, 75), (SILVER, 25))),
    Mine((180, 80, 80), ((GRANITE, 75), (SILVER, 20), (GOLD, 5))),
    Mine((120, 20, 120), ((OBSIDIAN, 75), (GOLD, 25))),
    Mine((120, 20, 120), ((OBSIDIAN, 75), (GOLD, 20), (SAPPHIRE, 5))),
    Mine((220, 220, 220), ((MARBLE, 75), (SAPPHIRE, 25))),
    Mine((220, 220, 220), ((MARBLE, 75), (SAPPHIRE, 20), (RUBY, 5))),
    Mine((120, 120, 120), ((SLATE, 75), (RUBY, 25))),
    Mine((120, 120, 120), ((SLATE, 75), (RUBY, 20), (EMERALD, 5))),
    Mine((160, 180, 180), ((SCHIST, 75), (EMERALD, 25))),
    Mine((160, 180, 180), ((SCHIST, 75), (EMERALD, 20), (DIAMOND, 5))),
    Mine((120, 170, 120), ((KIMBERLITE, 75), (DIAMOND, 25))),
    Mine((120, 170, 120), ((KIMBERLITE, 75), (DIAMOND, 20), (TITANIUM, 5))),
    Mine((180, 130, 0), ((MAGMA, 75), (TITANIUM, 25))),
    Mine((180, 130, 0), ((MAGMA, 75), (TITANIUM, 20), (MITHRIL, 5))),
]
