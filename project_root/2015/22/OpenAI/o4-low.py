import sys
from functools import lru_cache

def solve(boss_hp, boss_damage, hard):
    spells = {
        'missile': (53, 4, 0, 0, 0),
        'drain':   (73, 2, 0, 2, 0),
        'shield':  (113, 0, 7, 0, 6),
        'poison':  (173, 3, 0, 0, 6),
        'recharge':(229, 0, 0, 0, 5),
    }
    @lru_cache(None)
    def dfs(p_hp, p_mana, b_hp, t_shield, t_poison, t_recharge, turn, spent):
        if hard and turn==0:
            p_hp -= 1
            if p_hp<=0: return float('inf')
        armor = 7 if t_shield>0 else 0
        if t_poison>0: b_hp -= 3
        if t_recharge>0: p_mana += 101
        t_shield = max(0, t_shield-1)
        t_poison = max(0, t_poison-1)
        t_recharge = max(0, t_recharge-1)
        if b_hp<=0: return spent
        if turn==0:
            best = float('inf')
            for name,(cost,dmg,arm,heal,turns) in spells.items():
                if p_mana<cost: continue
                if name=='shield' and t_shield>0: continue
                if name=='poison' and t_poison>0: continue
                if name=='recharge' and t_recharge>0: continue
                nm = p_mana-cost
                nh = p_hp+heal
                nb = b_hp-dmg
                ts, tp, tr = t_shield, t_poison, t_recharge
                if name=='shield': ts = turns
                if name=='poison': tp = turns
                if name=='recharge': tr = turns
                spent2 = spent+cost
                val = dfs(nh, nm, nb, ts, tp, tr, 1, spent2)
                if val<best: best=val
            return best
        else:
            dmg = max(1, boss_damage - armor)
            p_hp -= dmg
            if p_hp<=0: return float('inf')
            return dfs(p_hp, p_mana, b_hp, t_shield, t_poison, t_recharge, 0, spent)
    return dfs(50,500,boss_hp,0,0,0,0,0)

data = [line.strip() for line in open(sys.argv[1])]
boss_hp = int(data[0].split()[-1])
boss_damage = int(data[1].split()[-1])
print(solve(boss_hp,boss_damage,False))
print(solve(boss_hp,boss_damage,True))