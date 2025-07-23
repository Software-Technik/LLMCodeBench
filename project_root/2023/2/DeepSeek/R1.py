import sys
from functools import reduce
from operator import mul

def is_possible(game_data, setup=None):
    if setup is None:
        setup = {"red": 12, "green": 13, "blue": 14}
    for game_set in game_data.split(';'):
        for cube in game_set.split(','):
            cube = cube.strip()
            if cube:
                n_str, color = cube.split(maxsplit=1)
                n = int(n_str)
                if n > setup[color]:
                    return False
    return True

def part1(lines, setup=None):
    if setup is None:
        setup = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for i, line in enumerate(lines, start=1):
        _, game_data = line.split(':', maxsplit=1)
        if is_possible(game_data.strip(), setup):
            total += i
    return total

def get_power(game_data):
    min_cubes = {}
    for set_str in game_data.split(';'):
        for cube in set_str.split(','):
            cube = cube.strip()
            if cube:
                n, color = cube.split(maxsplit=1)
                n_val = int(n)
                min_cubes[color] = max(min_cubes.get(color, 0), n_val)
    return reduce(mul, min_cubes.values())

def part2(lines):
    total = 0
    for line in lines:
        _, game_data = line.split(':', maxsplit=1)
        total += get_power(game_data.strip())
    return total

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [line.rstrip() for line in f]
    sys.stdout.write(f"{part1(lines)} {part2(lines)}")