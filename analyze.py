

MODE = 1


if MODE == 0:
    from main import MiningGame
    from world import World
    from mines import MINES
    game = MiningGame()
    for i in range(len(MINES)):
        game.world = World(15, i, game.world.regen)
        game.player.pos = [game.world.size / 2, game.world.size / 2]
        game.play()

if MODE == 1:
    from mines import MINES
    mine_vph = [sum(p * m.value for m, p in i.ores) / sum(p * m.health for m, p in i.ores) for i in MINES]

    for i in range(len(MINES)):
        print(f"{i}\t{mine_vph[i]}")

if MODE == 2:
    mine_level = 0
    tier = 0
    luck_level = 0
    k1 = 1
    hps = 10 + 2 * mine_level
    vph = mine_vph[tier]
    dpv = 10 + 2 * luck_level
    dps = dpv * vph * hps
    Lpd = 1 / (2 ** tier * 250)
    Lps = Lpd * dps
    Ltime = 1 / Lps

    mine_level_cost = mine_level * 10
    mine_level_per_second = k1 * mine_level_cost * dps

if MODE == 3:
    t = 0
    mine_level = 0

    for _ in range(50):
        vph = 1.0
        dpv = 1.0
        hps = 10 + 2 * mine_level
        dps = dpv * vph * hps
        print(f"{t}\t{dps}")
        mine_level_cost = (10 + 2 * mine_level) * 10
        mine_level_per_second = dps / mine_level_cost
        time_till_upgrade = 1 / mine_level_per_second
        t += time_till_upgrade
        mine_level += 1

if MODE == 4:
    t = 0
    mine_level = 0
    tier = 0
    luck_level = 0

    for _ in range(50):
        vph = 1 + tier
        dpv = 10 + 2 * luck_level
        hps = 10 + 2 * mine_level
        dps = dpv * vph * hps
        #print(f"{t}\t{dps}")
        mine_level_cost = (2 ** mine_level) * 10
        luck_level_cost = (2 ** luck_level) * 20
        tier_cost = 2 ** tier * 250
        mine_level_per_second = dps / mine_level_cost
        luck_level_per_second = dps / luck_level_cost
        tier_per_second = dps / tier_cost
        print(f"{t}\t{1/tier_per_second}")
        t += 1
        mine_level += mine_level_per_second
        luck_level += luck_level_per_second
        tier += tier_per_second

if MODE == 5:
    vph = 0.005
    marginal = 0.00125
    stone_v = 1
    stone_h = 200
    iron_v = stone_v + 1
    iron_h = ((stone_v * .75 + iron_v * .25) / (vph + marginal) - stone_h * .75) / .25
    gold_v = 1
    gold_h = 200

    print("%s\t%.5f\t%i\t%i" % (0, vph, stone_v, stone_h))
    for i in range(20):
        # 75/25 ratio
        vph = (stone_v * .75 + iron_v * .25) / (stone_h * .75 + iron_h * .25)
        print("%s\t%.5f\t%i\t%i\t%i\t%i" % (0, vph, stone_v, stone_h, iron_v, iron_h))

        # 75/20/5
        stone_r = .60
        iron_r = .25
        gold_r = .15

        gold_v = iron_v + i
        gold_h = int(((stone_v * stone_r + iron_v * iron_r + gold_v * gold_r) / (vph + marginal) - stone_h * stone_r - iron_h * iron_r) / gold_r)
        vph = (stone_v * stone_r + iron_v * iron_r + gold_v * gold_r) / (stone_h * stone_r + iron_h * iron_r + gold_h * gold_r)
        print("%s\t%.5f\t%i\t%i\t%i\t%i\t%i\t%i" % (0, vph, stone_v, stone_h, iron_v, iron_h, gold_v, gold_h))

        iron_v = gold_v
        iron_h = gold_h
        stone_v += 1
        stone_h = ((stone_v * .75 + iron_v * .25) / (vph + marginal) - iron_h * .25) / .75

if MODE == 6:
    vph = 0.005
    marginal = 0.00125
    stone_v = 1
    stone_h = 200
    iron_v = 2
    iron_h = 400
    gold_v = 3
    gold_h = 400

    print("%s\t%.5f\t%4i\t%4i" % (0, vph, stone_v, stone_h))
    for i in range(20):
        # 75/25 ratio
        vph = (stone_v * .75 + iron_v * .25) / (stone_h * .75 + iron_h * .25)
        print("%s\t%.5f\t%4i\t%4i\t%4i\t%4i" % (0, vph, stone_v, stone_h, iron_v, iron_h))

        # 75/20/5
        stone_r = .75
        iron_r = .20
        gold_r = .05

        gold_h += 400
        gold_v = ((vph + marginal) * (stone_h * stone_r + iron_h * iron_r + gold_h * gold_r) - stone_v * stone_r - iron_v * iron_r) / gold_r

        vph = (stone_v * stone_r + iron_v * iron_r + gold_v * gold_r) / (stone_h * stone_r + iron_h * iron_r + gold_h * gold_r)
        print("%s\t%.5f\t%4i\t%4i\t%4i\t%4i\t%4i\t%4i" % (0, vph, stone_v, stone_h, iron_v, iron_h, gold_v, gold_h))

        iron_v = gold_v
        iron_h = gold_h
        stone_h += 200
        stone_v = ((vph + marginal) * (stone_h * stone_r + iron_h * iron_r + gold_h * gold_r) - gold_v * gold_r - iron_v * iron_r) / stone_r

if MODE == 7:
    vph = 0.005
    stone_v = 1
    stone_h = 200
    iron_v = 2
    iron_h = 400
    gold_v = 3
    gold_h = 800

    print("%s\t%.5f\t%4i\t%4i" % (0, vph, stone_v, stone_h))
    for i in range(20):
        # 75/25 ratio

        vph = (stone_v * .75 + iron_v * .25) / (stone_h * .75 + iron_h * .25)
        print("%s\t%.5f\t%4i\t%4i\t%4i\t%4i" % (2*i + 1, vph, stone_v, stone_h, iron_v, iron_h))

        # 75/20/5
        stone_r = .75
        iron_r = .20
        gold_r = .05

        vph = (stone_v * stone_r + iron_v * iron_r + gold_v * gold_r) / (stone_h * stone_r + iron_h * iron_r + gold_h * gold_r)
        print("%s\t%.5f\t%4i\t%4i\t%4i\t%4i\t%4i\t%4i" % (2*i + 2, vph, stone_v, stone_h, iron_v, iron_h, gold_v, gold_h))

        iron_v = gold_v
        iron_h = gold_h
        gold_v += i + 2

        gold_h += 400

        stone_v += 1
        stone_h += 200

        """vph = (stone_v * .75 + iron_v * .25) / (stone_h * .75 + iron_h * .25)
        print("%s\t%.5f\t%4i\t%4i\t%4i\t%4i" % (0, vph, stone_v, stone_h, iron_v, iron_h))

        vph = (stone_v * stone_r + iron_v * iron_r + gold_v * gold_r) / (stone_h * stone_r + iron_h * iron_r + gold_h * gold_r)
        print("%s\t%.5f\t%4i\t%4i\t%4i\t%4i\t%4i\t%4i" % (0, vph, stone_v, stone_h, iron_v, iron_h, gold_v, gold_h))


        stone_v += 1
        stone_h += 200
        iron_v = gold_v
        iron_h = gold_h
        gold_v += i + 2
        gold_h += 400"""


