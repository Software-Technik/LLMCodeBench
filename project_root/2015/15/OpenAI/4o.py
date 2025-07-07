import sys
import math

def part1(data):
    ingredients = parse_ingredients(data)
    return get_max_score(ingredients, 100)

def part2(data):
    ingredients = parse_ingredients(data)
    return get_max_score(ingredients, 100, 500)

def parse_ingredients(data):
    return [
        {k: int(v) for k, v in (part.split(' ') for part in line.split(': ')[1].split(', '))}
        for line in data
    ]

def get_max_score(ingredients, total_sum, max_calories=-1):
    def score(choice):
        s = [0, 0, 0, 0]
        calories = 0
        for i, n in enumerate(choice):
            s[0] += n * ingredients[i]["capacity"]
            s[1] += n * ingredients[i]["durability"]
            s[2] += n * ingredients[i]["flavor"]
            s[3] += n * ingredients[i]["texture"]
            calories += n * ingredients[i]["calories"]
        return (math.prod(max(0, i) for i in s), calories)

    max_prod = 0
    for choice in get_permutations_from_sum(len(ingredients), total_sum):
        prod, calories = score(choice)
        if max_calories == -1 or calories == max_calories:
            max_prod = max(max_prod, prod)
    return max_prod

def get_permutations_from_sum(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in get_permutations_from_sum(length - 1, total_sum - value):
                yield (value,) + permutation

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")