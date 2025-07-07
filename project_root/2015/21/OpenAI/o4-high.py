import sys

l = open(sys.argv[1]).read().splitlines()
hp = int(l[0].split()[-1]); bd = int(l[1].split()[-1]); ba = int(l[2].split()[-1])
player_hp = 100
weapons = ((8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0))
armors = ((0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5))
rings = ((0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3))
rn = len(rings)
min_win = 10**9; max_lose = 0
for wc, wd, wa in weapons:
    for ac, ad, aa in armors:
        wac = wc + ac; wad = wd + ad; waa = wa + aa
        for i in range(rn):
            rc1, rd1, ra1 = rings[i]
            for j in range(i+1, rn):
                rc2, rd2, ra2 = rings[j]
                cost = wac + rc1 + rc2
                pd = wad + rd1 + rd2
                pa = waa + ra1 + ra2
                batk = bd - pa
                if batk < 1: batk = 1
                patk = pd - ba
                if patk < 1: patk = 1
                bt = (hp + patk - 1)//patk
                pt = (player_hp + batk - 1)//batk
                if pt >= bt:
                    if cost < min_win: min_win = cost
                else:
                    if cost > max_lose: max_lose = cost
sys.stdout.write(f"{min_win}\n{max_lose}\n")