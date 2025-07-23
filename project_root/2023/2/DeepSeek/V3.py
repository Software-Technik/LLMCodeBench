import sys
from functools import reduce
from operator import mul

def is_possible(game_data: str, setup=None) -> bool:
    if setup is None:
        setup = {"red": 12, "green": 13, "blue": 14}
    for game_set in game_data.split(';'):
        for cube_data in game_set.split(','):
            n, color = cube_data.strip().split(maxsplit=1)
            if int(n) > setup[color]:
                return False
    return True

def part1(text: str, setup=None) -> int:
    if setup is None:
        setup = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for i, line in enumerate(text.splitlines(), 1):
        game_data = line.split(':', 1)[1].strip()
        if is_possible(game_data, setup):
            total += i
    return total

def get_power(game_data: str) -> int:
    min_cubes = {}
    for game_set in game_data.split(';'):
        for cube_data in game_set.split(','):
            n, color = cube_data.strip().split(maxsplit=1)
            n = int(n)
            if color not in min_cubes or n > min_cubes[color]:
                min_cubes[color] = n
    return reduce(mul, min_cubes.values())

def part2(text: str) -> int:
    return sum(get_power(line.split(':', 1)[1].strip()) for line in text.splitlines())

with open(sys.argv[1]) as f:
    data = f.read()
print(f"{part1(data)} {part2(data)}")