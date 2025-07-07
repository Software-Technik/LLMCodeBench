import sys

def main():
    lines = [l.strip() for l in open(sys.argv[1])]
    boss_hp = int(lines[0].split()[-1])
    boss_dmg = int(lines[1].split()[-1])
    boss_armor = int(lines[2].split()[-1])
    player_hp = 100

    weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
    armors = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
    rings = [(0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
    ring_combs = [(rings[i],rings[j]) for i in range(len(rings)) for j in range(i+1,len(rings))]

    best_win = 10**9
    worst_lose = 0

    for c_w,d_w,a_w in weapons:
        for c_a,d_a,a_a in armors:
            for (c_r1,d_r1,a_r1),(c_r2,d_r2,a_r2) in ring_combs:
                cost = c_w+c_a+c_r1+c_r2
                dmg = d_w+d_a+d_r1+d_r2
                arm = a_w+a_a+a_r1+a_r2
                bd = max(1, boss_dmg - arm)
                pd = max(1, dmg - boss_armor)
                turns_to_die = (player_hp + bd - 1)//bd
                turns_to_kill = (boss_hp + pd - 1)//pd
                if turns_to_kill <= turns_to_die:
                    if cost < best_win: best_win = cost
                else:
                    if cost > worst_lose: worst_lose = cost

    sys.stdout.write(f"{best_win}\n{worst_lose}\n")

if __name__=="__main__":
    main()