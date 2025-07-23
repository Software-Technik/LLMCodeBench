import sys

def part1(data):
    player, boss, spells = get_game_data(data)
    return play(player, boss, {}, 0, spells, True)

def part2(data):
    player, boss, spells = get_game_data(data)
    return play(player, boss, {}, 0, spells, True, True)

def get_game_data(data):
    player = {
        "hp": 50,
        "armor": 0,
        "mana": 500,
    }
    boss = {
        "hp": int(data[0].split(": ")[1]),
        "damage": int(data[1].split(": ")[1]),
    }
    spells = {
        "missile": {"cost": 53, "damage": 4, "armor": 0, "heal_hp": 0, "heal_mana": 0, "turns": 0},
        "drain": {"cost": 73, "damage": 2, "armor": 0, "heal_hp": 2, "heal_mana": 0, "turns": 0},
        "shield": {"cost": 113, "damage": 0, "armor": 7, "heal_hp": 0, "heal_mana": 0, "turns": 6},
        "poison": {"cost": 173, "damage": 3, "armor": 0, "heal_hp": 0, "heal_mana": 0, "turns": 6},
        "recharge": {"cost": 229, "damage": 0, "armor": 0, "heal_hp": 0, "heal_mana": 101, "turns": 5},
    }
    return player, boss, spells

def play(player, boss, active_spells, spent_mana, spells, player_turn=True, part2=False, best_cost=None):
    if best_cost is not None and spent_mana >= best_cost:
        return best_cost

    active_spells_this_turn = {}
    for spell in active_spells:
        active_spells_this_turn[spell] = active_spells[spell].copy()
    player_this_turn = player.copy()
    boss_this_turn = boss.copy()

    if player_turn and part2:
        player_this_turn["hp"] -= 1
        if player_this_turn["hp"] <= 0:
            return best_cost

    expired = []
    for spell in active_spells_this_turn:
        player_this_turn["mana"] += active_spells_this_turn[spell]["heal_mana"]
        player_this_turn["hp"] += active_spells_this_turn[spell]["heal_hp"]
        boss_this_turn["hp"] -= active_spells_this_turn[spell]["damage"]
        active_spells_this_turn[spell]["turns"] -= 1
        if active_spells_this_turn[spell]["turns"] <= 0:
            expired.append(spell)

    for spell in expired:
        player_this_turn["armor"] -= active_spells_this_turn[spell]["armor"]
        del active_spells_this_turn[spell]

    if boss_this_turn["hp"] <= 0:
        return spent_mana if best_cost is None else min(best_cost, spent_mana)

    if player_turn:
        for spell in spells:
            if spell in active_spells_this_turn:
                continue
            if spells[spell]["cost"] > player_this_turn["mana"]:
                continue

            new_active_spells = {}
            for s in active_spells_this_turn:
                new_active_spells[s] = active_spells_this_turn[s].copy()
            new_player = player_this_turn.copy()

            new_player["mana"] -= spells[spell]["cost"]
            new_player["armor"] += spells[spell]["armor"]
            if spells[spell]["turns"] > 0:
                new_active_spells[spell] = spells[spell].copy()
                best_cost = play(new_player, boss_this_turn, new_active_spells, spent_mana + spells[spell]["cost"], spells, False, part2, best_cost)
            else:
                boss_copy = boss_this_turn.copy()
                boss_copy["hp"] -= spells[spell]["damage"]
                new_player["hp"] += spells[spell]["heal_hp"]
                best_cost = play(new_player, boss_copy, new_active_spells, spent_mana + spells[spell]["cost"], spells, False, part2, best_cost)
        return best_cost
    else:
        new_player = player_this_turn.copy()
        damage = max(1, boss_this_turn["damage"] - new_player["armor"])
        new_player["hp"] -= damage
        if new_player["hp"] > 0:
            return play(new_player, boss_this_turn, active_spells_this_turn, spent_mana, spells, True, part2, best_cost)
        return best_cost

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")