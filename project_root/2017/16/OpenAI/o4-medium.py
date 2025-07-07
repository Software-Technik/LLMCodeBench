import sys

def parse_instruction(inst):
    c = inst[0]
    if c == 's':
        return ('s', int(inst[1:]))
    elif c == 'x':
        a, b = inst[1:].split('/')
        return ('x', int(a), int(b))
    else:
        a, b = inst[1:].split('/')
        return ('p', a, b)

def dance(state, instrs):
    n = len(state)
    dancers = list(state)
    pos = {dancers[i]: i for i in range(n)}
    for op in instrs:
        t = op[0]
        if t == 's':
            x = op[1]
            dancers = dancers[-x:] + dancers[:-x]
            pos = {k: (v + x) % n for k, v in pos.items()}
        elif t == 'x':
            a, b = op[1], op[2]
            dancers[a], dancers[b] = dancers[b], dancers[a]
            pos[dancers[a]] = a
            pos[dancers[b]] = b
        else:
            a, b = op[1], op[2]
            pa, pb = pos[a], pos[b]
            dancers[pa], dancers[pb] = dancers[pb], dancers[pa]
            pos[a], pos[b] = pb, pa
    return ''.join(dancers)

def long_dance(init, instrs, iters):
    seen = []
    seen_idx = {}
    curr = init
    for i in range(iters):
        if curr in seen_idx:
            cycle = seen[seen_idx[curr]:]
            return cycle[(iters - seen_idx[curr]) % len(cycle)]
        seen_idx[curr] = i
        seen.append(curr)
        curr = dance(curr, instrs)
    return curr

if __name__ == '__main__':
    instrs = [parse_instruction(x) for x in open(sys.argv[1]).read().strip().split(',')]
    start = ''.join(chr(ord('a')+i) for i in range(16))
    print(dance(start, instrs))
    print(long_dance(start, instrs, 1000000000))