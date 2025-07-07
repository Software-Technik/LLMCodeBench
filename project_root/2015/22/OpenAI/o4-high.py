import sys

def solve(boss_hp_initial, boss_damage, hard):
    min_mana = 10**9
    def player_turn(p_hp, p_mana, b_hp, shield_t, poison_t, recharge_t, mana_spent):
        nonlocal min_mana
        if mana_spent >= min_mana:
            return
        if hard:
            p_hp -= 1
            if p_hp <= 0:
                return
        if shield_t > 0:
            armor = 7
        else:
            armor = 0
        if poison_t > 0:
            b_hp -= 3
        if recharge_t > 0:
            p_mana += 101
        shield_t -= 1
        poison_t -= 1
        recharge_t -= 1
        if b_hp <= 0:
            min_mana = mana_spent
            return
        if p_mana >= 53:
            nm = p_mana - 53
            ms = mana_spent + 53
            if ms < min_mana:
                pb = b_hp - 4
                if pb <= 0:
                    min_mana = ms
                else:
                    boss_turn(p_hp, nm, pb, shield_t, poison_t, recharge_t, ms)
        if p_mana >= 73:
            nm = p_mana - 73
            ms = mana_spent + 73
            if ms < min_mana:
                pb = b_hp - 2
                p2 = p_hp + 2
                if pb <= 0:
                    min_mana = ms
                else:
                    boss_turn(p2, nm, pb, shield_t, poison_t, recharge_t, ms)
        if p_mana >= 113 and shield_t <= 0:
            nm = p_mana - 113
            ms = mana_spent + 113
            if ms < min_mana:
                boss_turn(p_hp, nm, b_hp, 6, poison_t, recharge_t, ms)
        if p_mana >= 173 and poison_t <= 0:
            nm = p_mana - 173
            ms = mana_spent + 173
            if ms < min_mana:
                boss_turn(p_hp, nm, b_hp, shield_t, 6, recharge_t, ms)
        if p_mana >= 229 and recharge_t <= 0:
            nm = p_mana - 229
            ms = mana_spent + 229
            if ms < min_mana:
                boss_turn(p_hp, nm, b_hp, shield_t, poison_t, 5, ms)
    def boss_turn(p_hp, p_mana, b_hp, shield_t, poison_t, recharge_t, mana_spent):
        nonlocal min_mana
        if mana_spent >= min_mana:
            return
        if shield_t > 0:
            armor = 7
        else:
            armor = 0
        if poison_t > 0:
            b_hp -= 3
        if recharge_t > 0:
            p_mana += 101
        shield_t -= 1
        poison_t -= 1
        recharge_t -= 1
        if b_hp <= 0:
            min_mana = mana_spent
            return
        dmg = boss_damage - armor
        if dmg < 1:
            dmg = 1
        p_hp -= dmg
        if p_hp > 0:
            player_turn(p_hp, p_mana, b_hp, shield_t, poison_t, recharge_t, mana_spent)
    player_turn(50, 500, boss_hp_initial, 0, 0, 0, 0)
    return min_mana

if __name__ == "__main__":
    data = [line.strip() for line in open(sys.argv[1])]
    hp = int(data[0].split(": ")[1])
    dmg = int(data[1].split(": ")[1])
    print(solve(hp, dmg, False))
    print(solve(hp, dmg, True))