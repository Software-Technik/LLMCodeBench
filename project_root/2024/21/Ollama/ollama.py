import sys
from functools import lru_cache

def part1(lines):
    numeric_keys = {k: v for k, v in zip("7894561230A", [(i // 3, i % 3) for i in range(9)] + [[-1], [3, 1, 2]])}
    direction_keys = {"^": (0, 1), "v": (1, 2), "<": (1, 0), ">": (1, 2)}
    dd = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    @lru_cache(None)
    def ways(code, keypad):
        parts = []
        cur_loc = numeric_keys["A"]
        for c in code:
            next_loc = keypad[c]
            di, dj = next_loc[0] - cur_loc[0], next_loc[1] - cur_loc[1]
            moves = "v" * max(di, 0) + "^" * max(-di, 0) + ">" * max(dj, 0) + "<" * max(-dj, 0)
            combos = [''.join(p).strip('A') for p in set(permutations(moves)) if all((cur_loc[0] + di, cur_loc[1] + dj) in keypad.values() for di, dj in [dd[c] for c in p[:-1]])]
            parts.append(combos)
            cur_loc = next_loc
        return [''.join(x) for x in product(*parts)]

    def shortest3(code):
        ways1 = ways(code, numeric_keys)
        ways2 = (ways(way, direction_keys) for way in ways1)
        ways3 = (ways(way, direction_keys) for way in ways2)
        return min(len(way) for way in ways3)

    return sum(shortest3(line) * int(line[:-1]) for line in lines)

def part2(lines):
    numeric_keypad = {k: v for k, v in zip("7894561230A", [(i // 3, i % 3) for i in range(9)] + [[-1], [3, 1, 2]])}
    direction_keypad = {"^": (0, 1), "v": (1, 2), "<": (1, 0), ">": (1, 2)}
    dd = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    @lru_cache(None)
    def get_cost(a, b, keypad, depth=0):
        if not depth:
            assert keypad
            return min(len(x) for x in generate_ways(a, b))
        ways = set(generate_ways(a, b, keypad))
        if not ways:
            return float('inf')
        return min(get_cost(way[0], way[-1], True, depth - 1) + len(way) - 2 for way in ways)

    @lru_cache(None)
    def generate_ways(a, b):
        cur_loc = numeric_keys[a]
        next_loc = direction_keys[b]
        moves = ((m * max(dj if di == 0 else -di, 0) + m * max(di if dj < 0 else dj, 0)) for m in [">", "v"])
        return ["".join(p).strip('A') for p in permutations(moves) if all((cur_loc[0] + di, cur_loc[1] + dj) in direction_keys.values() for di, dj in [dd[c] for c in p[:-1]])]

    def get_code_cost(code, depth):
        return sum(get_cost(a, b, False, depth) for a, b in zip("A" + code, "A" + code[1:]))

    return sum(get_code_cost(line, 25) * int(line[:-1]) for line in lines)

input_path = sys.argv[1]
with open(input_path) as fin:
    for part, func in [(1, part1), (2, part2)]:
        print(f"Part {part}:", func(fin.read().strip().split("\n")))