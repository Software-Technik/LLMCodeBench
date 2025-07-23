import sys
from itertools import combinations, product
import math

def part1(data):
    player, boss, equipments = get_game_data(data)
    min_cost = float('inf')
    for equip in equipments:
        cost = equip[0]["cost"] + equip[1]["cost"] + equip[2][0]["cost"] + equip[2][1]["cost"]
        if cost >= min_cost:
            continue
        player["damage"] = equip[0]["damage"] + equip[1]["damage"] + equip[2][0]["damage"] + equip[2][1]["damage"]
        player["armor"] = equip[0]["armor"] + equip[1]["armor"] + equip[2][0]["armor"] + equip[2][1]["armor"]
        if battle(player, boss):
            min_cost = cost
    return min_cost

def part2(data):
    player, boss, equipments = get_game_data(data)
    max_cost = 0
    for equip in equipments:
        cost = equip[0]["cost"] + equip[1]["cost"] + equip[2][0]["cost"] + equip[2][1]["cost"]
        if cost <= max_cost:
            continue
        player["damage"] = equip[0]["damage"] + equip[1]["damage"] + equip[2][0]["damage"] + equip[2][1]["damage"]
        player["armor"] = equip[0]["armor"] + equip[1]["armor"] + equip[2][0]["armor"] + equip[2][1]["armor"]
        if not battle(player, boss):
            max_cost = cost
    return max_cost

def get_game_data(data):
    player = {
        "hp": 100,
        "damage": 0,
        "armor": 0,
    }
    boss = {
        "hp": int(data[0].split(": ")[1]),
        "damage": int(data[1].split(": ")[1]),
        "armor": int(data[2].split(": ")[1]),
    }
    weapons = [
        {"cost": 8, "damage": 4, "armor": 0},
        {"cost": 10, "damage": 5, "armor": 0},
        {"cost": 25, "damage": 6, "armor": 0},
        {"cost": 40, "damage": 7, "armor": 0},
        {"cost": 74, "damage": 8, "armor": 0},
    ]
    armors = [
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 13, "damage": 0, "armor": 1},
        {"cost": 31, "damage": 0, "armor": 2},
        {"cost": 53, "damage": 0, "armor": 3},
        {"cost": 75, "damage": 0, "armor": 4},
        {"cost": 102, "damage": 0, "armor": 5},
    ]
    rings = [
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 0, "damage": 0, "armor": 0},
        {"cost": 25, "damage": 1, "armor": 0},
        {"cost": 50, "damage": 2, "armor": 0},
        {"cost": 100, "damage": 3, "armor": 0},
        {"cost": 20, "damage": 0, "armor": 1},
        {"cost": 40, "damage": 0, "armor": 2},
        {"cost": 80, "damage": 0, "armor": 3},
    ]
    rings_combinations = list(combinations(rings, 2))
    equipments = list(product(weapons, armors, rings_combinations))
    return player, boss, equipments

def battle(player, boss):
    boss_hp = boss["hp"]
    player_hp = player["hp"]
    boss_attack = max(1, boss["damage"] - player["armor"])
    player_attack = max(1, player["damage"] - boss["armor"])
    boss_turns = math.ceil(boss_hp / player_attack)
    player_turns = math.ceil(player_hp / boss_attack)
    return player_turns >= boss_turns

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")