import sys

def step(state, rules):
    if not state: return set()
    mn, mx = min(state), max(state)
    new = set()
    for pot in range(mn-2, mx+3):
        n = (16 if pot-2 in state else 0) | (8 if pot-1 in state else 0) | (4 if pot in state else 0) | (2 if pot+1 in state else 0) | (1 if pot+2 in state else 0)
        if rules[n]: new.add(pot)
    return new

def main():
    lines = [l.rstrip('\n') for l in open(sys.argv[1])]
    init_str = lines[0][15:]
    rules = [0]*32
    for line in lines[2:]:
        if len(line) >= 10:
            pat, res = line[:5], line[9]
            idx = 0
            for c in pat: idx = (idx<<1) | (c=='#')
            if res == '#': rules[idx] = 1
    init = {i for i,c in enumerate(init_str) if c == '#'}
    state = set(init)
    for _ in range(20): state = step(state, rules)
    p1 = sum(state)
    state = set(init)
    last_score = sum(state)
    last_diff = 0
    cycle = 0
    while True:
        cycle += 1
        state = step(state, rules)
        sc = sum(state)
        diff = sc - last_score
        if diff == last_diff:
            p2 = sc + diff*(50000000000 - cycle)
            break
        last_diff = diff
        last_score = sc
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()