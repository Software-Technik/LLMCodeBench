import sys
from functools import reduce
from operator import mul

def is_possible(game_data: str, setup={"red": 12, "green": 13, "blue": 14}) -> bool:
    max_cubes = {"red": float("inf"), "green": float("inf"), "blue": float("inf")}
    for game_set in map(str.strip, game_data.split(';')):
        cubes_data = map(str.strip, game_set.split(','))
        for cube_data in cubes_data:
            n, color = cube_data.split(maxsplit=1)
            max_cubes[color] = min(int(n), setup[color])
            if max_cubes[color] < int(n):
                return False
    return True

def part1(text: str) -> int:
    total = 0
    for idx, line in enumerate(map(str.strip, text.splitlines()), start=1):
        _, game_data = line.split(":", 1)
        if is_possible(game_data):
            total += idx
    return total

def get_min_cubes_number(game_data: str) -> int:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for game_set in map(str.strip, game_data.split(';')):
        cubes_data = map(str.strip, game_set.split(','))
        for cube_data in cubes_data:
            n, color = cube_data.split(maxsplit=1)
            max_cubes[color] = max(int(n), max_cubes[color])
    return reduce(mul, (max_cubes[cube] for cube in max_cubes), 1)

def part2(text: str) -> int:
    total = sum(get_min_cubes_number(line.split(":", 1)[1].strip()) for line in map(str.strip, text.splitlines()))
    return total

with open(sys.argv[1]) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")