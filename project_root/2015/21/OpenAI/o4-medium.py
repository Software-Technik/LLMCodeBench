import sys
from itertools import combinations

lines = open(sys.argv[1]).read().splitlines()
boss_hp = int(lines[0].split(': ')[1])
boss_dmg = int(lines[1].split(': ')[1])
boss_arm = int(lines[2].split(': ')[1])
weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armors = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings = [(0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
ring_combos = list(combinations(rings,2))
min_win = 10**9
max_loss = 0
for wc,wd,wa in weapons:
    for ac,ad,aa in armors:
        for (r1c,r1d,r1a),(r2c,r2d,r2a) in ring_combos:
            cost = wc+ac+r1c+r2c
            dmg_tot = wd+ad+r1d+r2d
            arm_tot = wa+aa+r1a+r2a
            p_dmg = dmg_tot - boss_arm
            if p_dmg < 1: p_dmg = 1
            b_dmg = boss_dmg - arm_tot
            if b_dmg < 1: b_dmg = 1
            t_b = (boss_hp + p_dmg - 1)//p_dmg
            t_p = (100 + b_dmg - 1)//b_dmg
            if t_p >= t_b:
                if cost < min_win: min_win = cost
            else:
                if cost > max_loss: max_loss = cost
sys.stdout.write(f"{min_win}\n{max_loss}\n")