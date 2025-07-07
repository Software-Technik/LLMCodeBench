import sys
from functools import reduce
from operator import mul

def is_possible(game_data: str, setup={"red": 12, "green": 13, "blue": 14}) -> bool:
    for game_set in game_data.split(";"):
        for cube_data in game_set.split(","):
            n, color = cube_data.split()
            if int(n) > setup[color]:
                return False
    return True

def part1(text: str, setup={"red": 12, "green": 13, "blue": 14}) -> int:
    return sum(i for i, line in enumerate(text.splitlines(), start=1) if is_possible(line.split(":", 1)[1].strip(), setup))

def get_power(game_data: str) -> int:
    min_cubes_number = {}
    for game_set in game_data.split(";"):
        for cube_data in game_set.split(","):
            n, color = cube_data.split()
            n = int(n)
            if n > min_cubes_number.get(color, 0):
                min_cubes_number[color] = n
    return reduce(mul, min_cubes_number.values(), 1)

def part2(text: str) -> int:
    return sum(get_power(line.split(":", 1)[1].strip()) for line in text.splitlines())

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}")