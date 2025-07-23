import sys
from itertools import permutations, product, combinations
from functools import lru_cache

def part1(lines):
    numeric_keys = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
    }
    direction_keys = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
    dd = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    @lru_cache(maxsize=None)
    def get_moves(cur_loc, next_loc):
        di = next_loc[0] - cur_loc[0]
        dj = next_loc[1] - cur_loc[1]
        moves = []
        if di > 0:
            moves.append(("v", di))
        elif di < 0:
            moves.append(("^", -di))
        if dj > 0:
            moves.append((">", dj))
        elif dj < 0:
            moves.append(("<", -dj))
        return moves

    def generate_combos(moves):
        total_moves = sum(count for _, count in moves)
        directions = []
        for d, cnt in moves:
            directions.extend([d] * cnt)
        unique_perms = set(permutations(directions))
        return [''.join(p) + 'A' for p in unique_perms]

    def is_valid_path(start, path, keypad):
        ci, cj = start
        for c in path[:-1]:
            di, dj = dd[c]
            ci += di
            cj += dj
            if (ci, cj) not in keypad.values():
                return False
        return True

    def ways(code, keypad):
        parts = []
        cur_loc = keypad["A"]
        for c in code:
            next_loc = keypad[c]
            moves = get_moves(cur_loc, next_loc)
            if not moves:
                parts.append(['A'])
                continue
            combos = generate_combos(moves)
            valid_combos = [combo for combo in combos if is_valid_path(cur_loc, combo, keypad)]
            parts.append(valid_combos)
            cur_loc = next_loc
        return ["".join(x) for x in product(*parts)]

    def shortest3(code):
        ways1 = ways(code, numeric_keys)
        ways2 = []
        for way in ways1:
            ways2.extend(ways(way, direction_keys))
        ways3 = []
        for way in ways2:
            ways3.extend(ways(way, direction_keys))
        return min(len(x) for x in ways3) if ways3 else 0

    ans = 0
    for line in lines:
        ans += shortest3(line) * int(line[:-1])
    return ans

def part2(lines):
    numeric_keypad = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
    }
    direction_keypad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
    dd = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    @lru_cache(maxsize=None)
    def get_moves(a, b, keypad_type):
        keypad = direction_keypad if keypad_type else numeric_keypad
        cur_loc = keypad[a]
        next_loc = keypad[b]
        di = next_loc[0] - cur_loc[0]
        dj = next_loc[1] - cur_loc[1]
        moves = []
        if di > 0:
            moves.append(("v", di))
        elif di < 0:
            moves.append(("^", -di))
        if dj > 0:
            moves.append((">", dj))
        elif dj < 0:
            moves.append(("<", -dj))
        return moves

    @lru_cache(maxsize=None)
    def generate_combos(a, b, keypad_type):
        moves = get_moves(a, b, keypad_type)
        total_moves = sum(count for _, count in moves)
        directions = []
        for d, cnt in moves:
            directions.extend([d] * cnt)
        unique_perms = set(permutations(directions))
        return [''.join(p) + 'A' for p in unique_perms]

    @lru_cache(maxsize=None)
    def is_valid_path(a, path, keypad_type):
        keypad = direction_keypad if keypad_type else numeric_keypad
        ci, cj = keypad[a]
        for c in path[:-1]:
            di, dj = dd[c]
            ci += di
            cj += dj
            if (ci, cj) not in keypad.values():
                return False
        return True

    @lru_cache(maxsize=None)
    def get_cost(a, b, keypad_type, depth=0):
        if depth == 0:
            combos = generate_combos(a, b, True)
            valid_combos = [combo for combo in combos if is_valid_path(a, combo, True)]
            return min(len(x) for x in valid_combos) if valid_combos else float('inf')

        combos = generate_combos(a, b, keypad_type)
        valid_combos = [combo for combo in combos if is_valid_path(a, combo, keypad_type)]
        min_cost = float('inf')
        for seq in valid_combos:
            seq = "A" + seq
            cost = 0
            for i in range(len(seq) - 1):
                cost += get_cost(seq[i], seq[i + 1], True, depth - 1)
            min_cost = min(min_cost, cost)
        return min_cost

    def get_code_cost(code, depth):
        code = "A" + code
        cost = 0
        for i in range(len(code) - 1):
            cost += get_cost(code[i], code[i + 1], False, depth)
        return cost

    ans = 0
    for line in lines:
        ans += get_code_cost(line, 25) * int(line[:-1])
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))