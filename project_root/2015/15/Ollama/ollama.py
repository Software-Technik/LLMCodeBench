import sys
import math

def part1(data):
    ingredients = parse_ingredients(data)
    return get_max_score(ingredients, 100)

def part2(data):
    ingredients = parse_ingredients(data)
    return get_max_score(ingredients, 500, True)

def parse_ingredients(data):
    ingredients = [tuple(map(int, line.split(": ")[1].split(", "))) for line in data]
    return tuple(tuple(x[i] for x in ingredients) for i in range(4))

def score(nutrients):
    s = [max(0, nuts[0] - 3 * nuts[1]) + nutrients[2] - 2 * nutrients[3] for nuts in zip(*nutrients)]
    return math.prod(s)

def get_max_score(ingredients, total_calories, is_part2=False):
    result = 0
    stack = [(total_calories, (0, 0, 0))]

    while stack:
        remaining, current_scores = stack.pop()
        if not any(current_scores):
            result = max(result, score([current_scores]))
        else:
            for i in range(len(ingredients)):
                new_remaining = remaining - ingredients[i][1]
                if new_remaining >= 0:
                    nscores = tuple(c + d * ingredients[i][j] for j, c in enumerate(current_scores))
                    stack.append((new_remaining, nscores))

    return result

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")