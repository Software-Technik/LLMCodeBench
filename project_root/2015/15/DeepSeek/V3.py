import sys
import math
from itertools import product

def part1(data):
    ingredients = list(parse_ingredients(data).values())
    return get_max_score(ingredients, 100)

def part2(data):
    ingredients = list(parse_ingredients(data).values())
    return get_max_score(ingredients, 100, 500)

def parse_ingredients(data):
    ingredients = {}
    for line in data:
        parts = line.split(": ")
        name = parts[0]
        ingredients[name] = {}
        parts2 = parts[1].split(", ")
        for part in parts2:
            parts3 = part.split(" ")
            ingredients[name][parts3[0]] = int(parts3[1])
    return ingredients

def get_max_score(ingredients, total_sum, max_calories=-1):
    max_score = 0
    n = len(ingredients)
    if n == 4:
        for a in range(total_sum + 1):
            for b in range(total_sum - a + 1):
                for c in range(total_sum - a - b + 1):
                    d = total_sum - a - b - c
                    s = [0, 0, 0, 0]
                    calories = 0
                    for i, n in enumerate((a, b, c, d)):
                        s[0] += n * ingredients[i]["capacity"]
                        s[1] += n * ingredients[i]["durability"]
                        s[2] += n * ingredients[i]["flavor"]
                        s[3] += n * ingredients[i]["texture"]
                        calories += n * ingredients[i]["calories"]
                    s = [max(0, x) for x in s]
                    if max_calories == -1 or calories == max_calories:
                        current_score = math.prod(s)
                        if current_score > max_score:
                            max_score = current_score
    return max_score

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")