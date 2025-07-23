import sys
from itertools import combinations, product
import math

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
    rings = {
        "none1": {"cost": 0, "damage": 0, "armor": 0},
        "none2": {"cost": 0, "damage": 0, "armor": 0},
        "damage1": {"cost": 25, "damage": 1, "armor": 0},
        "damage2": {"cost": 50, "damage": 2, "armor": 0},
        "damage3": {"cost": 100, "damage": 3, "armor": 0},
        "defense1": {"cost": 20, "damage": 0, "armor": 1},
        "defense2": {"cost": 40, "damage": 0, "armor": 2},
        "defense3": {"cost": 80, "damage": 0, "armor": 3},
    }

    rings_combinations = list(combinations(rings.values(), 2))
    equipments = product(weapons.values(), armors.values(), rings_combinations)

    return player, boss, equipments

def battle(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    player_attack = max(1, player_damage - boss_armor)
    boss_attack = max(1, boss_damage - player_armor)
    boss_turns = math.ceil(boss_hp / player_attack)
    player_turns = math.ceil(player_hp / boss_attack)
    return player_turns >= boss_turns

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

player, boss, equipments = get_game_data(data)
wins = []
losses = []
for equip in equipments:
    cost = equip[0]['cost'] + equip[1]['cost'] + equip[2][0]['cost'] + equip[2][1]['cost']
    damage = equip[0]['damage'] + equip[1]['damage'] + equip[2][0]['damage'] + equip[2][1]['damage']
    armor = equip[0]['armor'] + equip[1]['armor'] + equip[2][0]['armor'] + equip[2][1]['armor']
    if battle(100, damage, armor, boss['hp'], boss['damage'], boss['armor']):
        wins.append(cost)
    else:
        losses.append(cost)

part1 = min(wins)
part2 = max(losses)
sys.stdout.write(f"{part1}\n{part2}\n")