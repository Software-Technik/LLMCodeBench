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

def play(player, boss, active_spells, spent_mana, spells, player_turn=True, part2=False, best_cost=float('inf')):
    if spent_mana >= best_cost:
        return best_cost

    player_this_turn = dict(player)
    boss_this_turn = dict(boss)
    active_spells_this_turn = {spell: dict(effect) for spell, effect in active_spells.items()}

    if player_turn and part2:
        player_this_turn["hp"] -= 1
        if player_this_turn["hp"] <= 0:
            return best_cost

    for spell in list(active_spells_this_turn.keys()):
        if active_spells_this_turn[spell]["turns"] > 0:
            player_this_turn["mana"] += active_spells_this_turn[spell]["heal_mana"]
            player_this_turn["hp"] += active_spells_this_turn[spell]["heal_hp"]
            boss_this_turn["hp"] -= active_spells_this_turn[spell]["damage"]
            active_spells_this_turn[spell]["turns"] -= 1
        if active_spells_this_turn[spell]["turns"] == 0:
            player_this_turn["armor"] -= active_spells_this_turn[spell]["armor"]
            del active_spells_this_turn[spell]

    if boss_this_turn["hp"] <= 0:
        return spent_mana
    
    if player_turn:
        for spell, properties in spells.items():
            if spell not in active_spells_this_turn and properties["cost"] <= player_this_turn["mana"]:
                new_active_spells = dict(active_spells_this_turn)
                new_player = dict(player_this_turn)
                new_boss = dict(boss_this_turn)

                new_player["mana"] -= properties["cost"]
                if properties["turns"] > 0:
                    new_player["armor"] += properties["armor"]
                    new_active_spells[spell] = dict(properties)
                else:
                    new_boss["hp"] -= properties["damage"]
                    new_player["hp"] += properties["heal_hp"]

                best_cost = play(new_player, new_boss, new_active_spells, spent_mana + properties["cost"], spells, False, part2, best_cost)
    else:
        new_player = dict(player_this_turn)
        new_player["hp"] -= max(1, boss_this_turn["damage"] - new_player["armor"])
        if new_player["hp"] > 0:
            return play(new_player, boss_this_turn, active_spells_this_turn, spent_mana, spells, True, part2, best_cost)

    return best_cost

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")