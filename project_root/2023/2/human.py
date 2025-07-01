import sys
from functools import reduce
from operator import mul



def is_possible(game_data: str, setup={"red": 12, "green": 13, "blue": 14}) -> bool:
    for game_set in game_data.split(";"):
        cubes_data = game_set.strip().split(",")
        for cube_data in cubes_data:
            n, color = cube_data.strip().split(maxsplit=1)
            n = int(n)
            if n > setup[color]:
                return False
    return True


def part1(text: str, setup={"red": 12, "green": 13, "blue": 14}) -> int:
    total = 0
    for i, line in enumerate(text.splitlines(), start=1):
        _, game_data = line.split(":", maxsplit=1)
        if is_possible(game_data.strip(), setup):
            total += i
    return total

def get_power(game_data: str) -> int:
    min_cubes_number = {}
    for game_set in game_data.split(";"):
        cubes_data = game_set.strip().split(",")
        for cube_data in cubes_data:
            n, color = cube_data.strip().split(maxsplit=1)
            n = int(n)
            min_cubes_number.setdefault(color, n)
            if n > min_cubes_number[color]:
                min_cubes_number[color] = n
    return reduce(mul, min_cubes_number.values())


def part2(text: str) -> int:
    total = 0
    for line in text.splitlines():
        _, game_data = line.split(":", maxsplit=1)
        power = get_power(game_data.strip())
        total += power
    return total


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")

