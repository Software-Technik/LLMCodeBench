import sys
from itertools import permutations, combinations
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

    def ways(code, keypad):
        parts = []
        cur_loc = keypad["A"]
        for c in code:
            next_loc = keypad[c]
            di = next_loc[0] - cur_loc[0]
            dj = next_loc[1] - cur_loc[1]
            moves = ""
            if di > 0:
                moves += "v" * di
            elif di < 0:
                moves += "^" * -di
            if dj > 0:
                moves += ">" * dj
            elif dj < 0:
                moves += "<" * -dj
            raw_combos = set("".join(x) + "A" for x in permutations(moves))
            combos = []
            for combo in raw_combos:
                ci, cj = cur_loc
                good = True
                for c in combo[:-1]:
                    di, dj = dd[c]
                    ci, cj = ci + di, cj + dj
                    if not (ci, cj) in keypad.values():
                        good = False
                        break
                if good:
                    combos.append(combo)
            parts.append(combos)
            cur_loc = next_loc
        return ["".join(x) for x in product(*parts)]

    def shortest3(code):
        ways1 = ways(code, numeric_keys)
        ways2 = (way2 for way1 in ways1 for way2 in ways(way1, direction_keys))
        ways3 = (way3 for way2 in ways2 for way3 in ways(way2, direction_keys))
        return min(len(x) for x in ways3)

    ans = sum(shortest3(line) * int(line[:-1]) for line in lines)

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
    
    def get_combos(ca, a, cb, b):
        for idxs in combinations(range(a + b), r=a):
            res = [cb] * (a + b)
            for i in idxs:
                res[i] = ca
            yield "".join(res)

    @lru_cache(None)
    def generate_ways(a, b, keypad):
        keypad = direction_keypad if keypad else numeric_keypad
        cur_loc = keypad[a]
        next_loc = keypad[b]
        di = next_loc[0] - cur_loc[0]
        dj = next_loc[1] - cur_loc[1]
        moves = []
        if di > 0:
            moves += ["v", di]
        else:
            moves += ["^", -di]
        if dj > 0:
            moves += [">", dj]
        else:
            moves += ["<", -dj]
        raw_combos = {"".join(x) + "A" for x in get_combos(*moves)}
        combos = []
        for combo in raw_combos:
            ci, cj = cur_loc
            good = all((ci + dd[c][0], cj + dd[c][1]) in keypad.values() for c in combo[:-1])
            if good:
                combos.append(combo)
        return combos

    @lru_cache(None)
    def get_cost(a, b, keypad, depth=0):
        if depth == 0:
            return min(len(x) for x in generate_ways(a, b, True))
        best_cost = float('inf')
        for seq in generate_ways(a, b, keypad):
            cost = sum(get_cost(seq[i], seq[i + 1], True, depth - 1) for i in range(len(seq) - 1))
            best_cost = min(best_cost, cost)
        return best_cost

    def get_code_cost(code, depth):
        code = "A" + code
        return sum(get_cost(code[i], code[i + 1], False, depth) for i in range(len(code) - 1))

    ans = sum(get_code_cost(line, 25) * int(line[:-1]) for line in lines)

    return ans

input_path = sys.argv[1]

with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))