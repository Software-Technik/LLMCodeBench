import sys
from functools import lru_cache
from itertools import combinations

numeric_keypad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2),
}
direction_keypad = {
    '^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}
numeric_pos = set(numeric_keypad.values())
direction_pos = set(direction_keypad.values())
dd = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}

def get_combos(ca, a, cb, b):
    for idxs in combinations(range(a + b), a):
        res = [cb] * (a + b)
        for i in idxs:
            res[i] = ca
        yield ''.join(res)

@lru_cache(None)
def generate_ways(a, b, is_dir):
    keypad = direction_keypad if is_dir else numeric_keypad
    pos_set = direction_pos if is_dir else numeric_pos
    ci, cj = keypad[a]
    ni, nj = keypad[b]
    di, dj = ni - ci, nj - cj
    ca, a_cnt = ('v', di) if di > 0 else ('^', -di)
    cb, b_cnt = ('>', dj) if dj > 0 else ('<', -dj)
    combos = []
    for seq in get_combos(ca, a_cnt, cb, b_cnt):
        combo = seq + "A"
        x, y = ci, cj
        ok = True
        for c in combo[:-1]:
            dx, dy = dd[c]
            x += dx; y += dy
            if (x, y) not in pos_set:
                ok = False
                break
        if ok:
            combos.append(combo)
    return combos

@lru_cache(None)
def get_cost(a, b, is_dir, depth):
    if depth == 0:
        return min(len(x) for x in generate_ways(a, b, True))
    best = 1 << 60
    for seq in generate_ways(a, b, is_dir):
        total = 0
        full = 'A' + seq
        for i in range(len(full) - 1):
            total += get_cost(full[i], full[i+1], True, depth - 1)
            if total >= best:
                break
        if total < best:
            best = total
    return best

def get_code_cost(code, depth):
    full = 'A' + code
    total = 0
    for i in range(len(full) - 1):
        total += get_cost(full[i], full[i+1], False, depth)
    return total

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    ans1 = ans2 = 0
    for line in lines:
        cnt = int(line[:-1])
        ans1 += get_code_cost(line, 2) * cnt
        ans2 += get_code_cost(line, 25) * cnt
    print(ans1, ans2)

if __name__ == '__main__':
    main()