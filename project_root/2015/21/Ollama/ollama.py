import sys
from itertools import combinations, product
import math

def part1(data):
    player, boss, equipments = get_game_data(data)
    min_cost = float('inf')
    for equip in equipments:
        cost = sum(item["cost"] for item in equip)
        if battle(player, boss, equip):
            min_cost = min(min_cost, cost)
    return min_cost

def part2(data):
    player, boss, equipments = get_game_data(data)
    max_cost = float('-inf')
    for equip in equipments:
        cost = sum(item["cost"] for item in equip)
        if not battle(player, boss, equip):
            max_cost = max(max_cost, cost)
    return max_cost

def get_game_data(data):
    player = {"hp": 100, "damage": 0, "armor": 0}
    boss = {
        "hp": int(data[0].split(": ")[1]),
        "damage": int(data[1].split(": ")[1]),
        "armor": int(data[2].split(": ")[1]),
    }
    weapons = {
        "dagger": {"cost": 8, "damage": 4, "armor": 0},
        "shortsword": {"cost": 10, "damage": 5, "armor": 0},
        "warhammer": {"cost": 25, "damage": 6, "armor": 0},
        "longsword": {"cost": 40, "damage": 7, "armor": 0},
        "greataxe": {"cost": 74, "damage": 8, "armor": 0},
    }
    armors = {
        "none": {"cost": 0, "damage": 0, "armor": 0},
        "leather": {"cost": 13, "damage": 0, "armor": 1},
        "chainmail": {"cost": 31, "damage": 0, "armor": 2},
        "splintmail": {"cost": 53, "damage": 0, "armor": 3},
        "bandedmail": {"cost": 75, "damage": 0, "armor": 4},
        "platemail": {"cost": 102, "damage": 0, "armor": 5},
    }
    rings = list(rings.values())
    rings_combinations = list(combinations(rings, 2))
    equipments = list(product(weapons.values(), armors.values(), rings_combinations))
    return player, boss, equipments

def battle(player, boss, equip):
    dmg = sum(item["damage"] for item in equip)
    armor = sum(item["armor"] for item in equip)
    player["damage"], player["armor"] = dmg, armor
    player_hp, boss_hp = player["hp"], boss["hp"]
    player_attack = max(1, dmg - boss["armor"])
    boss_attack = max(1, boss["damage"] - armor)
    player_turns = math.ceil(boss_hp / player_attack)
    return player_turns * boss_attack <= player_hp

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")