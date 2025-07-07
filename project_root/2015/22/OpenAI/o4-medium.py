import sys
sys.setrecursionlimit(10000)
data = open(sys.argv[1]).read().splitlines()
boss_start_hp = int(data[0].split(": ")[1])
boss_damage = int(data[1].split(": ")[1])

def solve(hard):
    best = [10**9]
    def dfs(p_hp, p_mana, b_hp, sh, po, re, spent, player_turn):
        if spent >= best[0]:
            return
        if player_turn:
            if hard:
                p_hp -= 1
                if p_hp <= 0:
                    return
        armor = 7 if sh > 0 else 0
        if po > 0:
            b_hp -= 3
        if re > 0:
            p_mana += 101
        sh2 = sh-1 if sh>0 else 0
        po2 = po-1 if po>0 else 0
        re2 = re-1 if re>0 else 0
        if b_hp <= 0:
            best[0] = spent
            return
        if player_turn:
            # missile
            if p_mana >= 53:
                dfs(p_hp, p_mana-53, b_hp-4, sh2, po2, re2, spent+53, False)
            # drain
            if p_mana >= 73:
                dfs(p_hp+2, p_mana-73, b_hp-2, sh2, po2, re2, spent+73, False)
            # shield
            if p_mana >= 113 and sh2 == 0:
                dfs(p_hp, p_mana-113, b_hp, 6, po2, re2, spent+113, False)
            # poison
            if p_mana >= 173 and po2 == 0:
                dfs(p_hp, p_mana-173, b_hp, sh2, 6, re2, spent+173, False)
            # recharge
            if p_mana >= 229 and re2 == 0:
                dfs(p_hp, p_mana-229, b_hp, sh2, po2, 5, spent+229, False)
        else:
            dmg = boss_damage - armor
            if dmg < 1:
                dmg = 1
            p_hp -= dmg
            if p_hp > 0:
                dfs(p_hp, p_mana, b_hp, sh2, po2, re2, spent, True)
    dfs(50, 500, boss_start_hp, 0, 0, 0, 0, True)
    return best[0]

print(solve(False))
print(solve(True))