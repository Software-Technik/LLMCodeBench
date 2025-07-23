import sys

def part1(data):
    player, boss, spells = get_game_data(data)
    return play(player, boss, {}, 0, spells)

def part2(data):
    player, boss, spells = get_game_data(data)
    return min(play(player, boss, {}, cost, spells) for cost in range(501, 10000))

def get_game_data(data):
    player = {"hp": 50, "armor": 0, "mana": 500}
    boss = {
        "hp": int(data[0].split(": ")[1]),
        "damage": int(data[1].split(": ")[1]),
    }
    spells = [
        {"cost": 53, "effect": lambda p, b: ({"hp": p["hp"]}, {"hp": b["hp"] - 4})},
        {"cost": 73, "effect": lambda p, b: ({"mana": p["mana"] + 2, "hp": p["hp"] + 2}, {"hp": b["hp"] - 2})},
        {"cost": 113, "effect_duration": 6,
            "turn_effect": [lambda p: ({"armor": 7}, {})] * 5 +
                             [lambda p: ({"armor": 0}, {})],
            "instant_effect": lambda p, b: None},
        {"cost": 173, "effect_duration": 6,
            "turn_effect": [lambda p: ({}, {"hp": b.get("hp", boss["hp"]) - 3})] * 5 +
                             [lambda p: ({"armor": 0}, {})],
            "instant_effect": lambda p, b: None},
        {"cost": 229, "effect_duration": 5,
            "turn_effect": [lambda p: ({"mana": p["mana"] + 101}, {})] * 4 +
                             [lambda p: ({"armor": 0}, {})],
            "instant_effect": lambda p, b: None},
             ]
    return player, boss, spells

def play(player, boss, active_spells, spent_mana, spells):
    player = player.copy()
    boss = boss.copy()

    if not any(duration > 1 for e in active_spells.values() for duration in [e.get("effect_duration", 0)]):
        return
    for effect in active_spells:
        delta_player, delta_boss = effect["turn_effect"][active_spells[effect]["duration"] - 1](player)
        player.update(delta_player)
        boss.update(delta_boss)
        if not player["hp"]:
            return None
        if not boss["hp"]:
            return spent_mana

    player["armor"], _, player["mana"] = sorted((player[k] for k in "armor", "mana"), key=int)[-2:]
        max_spell_cost = player["mana"]
    min_winning_cost = None
    for spell in spells:
        if not 0 < len(active_spells) < (spell.get("effect_duration", 0) + 1):
            continue
        cost, effect, duration, instant_effect = spell["cost"], spell["turn_effect"][0], spell.get("effect_duration", 0), spell["instant_effect"]
        if (max_spell_cost >= cost and min_winning_cost is None or max_min_winning_cost < cost) or (
            any(e[duration]["instant_effect"] is instant_effect for e in active_spells.values())):
            continue

        new_player, new_boss = player.copy(), boss.copy()
        delta_player, delta_boss, effects_in_duration_remaining = 0
        duration -= len(active_spells)
        for _ in range(duration):
            delta_p, delta_d = effect(new_player, new_boss)
            if not (delta_p is None or effects_in_duration_remaining == duration):
                delta_p.update({"armor": player["armor"]})
                new_p.remaining_duration -= 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")