import sys
from itertools import permutations, product
from itertools import product, combinations
from functools import lru_cache
from collections import deque

def find_shortest_paths(start, goal, valid_positions, dd):
    dist = {}
    q = deque([start])
    dist[start] = 0
    min_dist = None
    while q:
        i, j = q.popleft()
        if (i, j) == goal:
            min_dist = dist[(i, j)]
            break
        for di, dj in dd.values():
            ni, nj = i + di, j + dj
            if (ni, nj) in valid_positions:
                if (ni, nj) not in dist:
                    dist[(ni, nj)] = dist[(i, j)] + 1
                    q.append((ni, nj))
    if min_dist is None:
        return []
    paths = []
    stack = [(start, [])]
    while stack:
        (i, j), path = stack.pop()
        if (i, j) == goal:
            if len(path) == min_dist:
                paths.append("".join(path))
            continue
        if len(path) >= min_dist:
            continue
        for move, (di, dj) in dd.items():
            ni, nj = i + di, j + dj
            if (ni, nj) in valid_positions:
                stack.append(((ni, nj), path + [move]))
    return paths

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
        valid_positions = set(keypad.values())
        for c in code:
            next_loc = keypad[c]
            paths = find_shortest_paths(cur_loc, next_loc, valid_positions, dd)
            combos = [p + 'A' for p in paths]
            parts.append(combos)
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
        return min([len(x) for x in ways3])

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

    @lru_cache(None)
    def generate_ways(a, b, keypad):
        keypad_dict = direction_keypad if keypad else numeric_keypad
        start = keypad_dict[a]
        goal = keypad_dict[b]
        valid_positions = set(keypad_dict.values())
        paths = find_shortest_paths(start, goal, valid_positions, dd)
        return [p + 'A' for p in paths]

    @lru_cache(None)
    def get_cost(a, b, keypad, depth=0):
        if depth == 0:
            return min([len(x) for x in generate_ways(a, b, True)])
        ways_list = generate_ways(a, b, keypad)
        best_cost = 1 << 60
        for seq in ways_list:
            seq = "A" + seq
            cost = 0
            for i in range(len(seq) - 1):
                a_char, b_char = seq[i], seq[i+1]
                cost += get_cost(a_char, b_char, True, depth - 1)
            best_cost = min(best_cost, cost)
        return best_cost

    def get_code_cost(code, depth):
        code = "A" + code
        cost = 0
        for i in range(len(code) - 1):
            a, b = code[i], code[i+1]
            cost += get_cost(a, b, False, depth)
        return cost

    ans = 0
    for line in lines:
        ans += get_code_cost(line, 25) * int(line[:-1])
    return ans

input_path = sys.argv[1]

with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))