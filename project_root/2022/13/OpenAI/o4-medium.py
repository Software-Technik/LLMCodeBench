import sys, json
from functools import cmp_to_key
def compare(a, b):
    if type(a) is int and type(b) is int:
        return a - b
    if type(a) is int:
        return compare([a], b)
    if type(b) is int:
        return compare(a, [b])
    for x, y in zip(a, b):
        c = compare(x, y)
        if c:
            return c
    return len(a) - len(b)
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f if l.strip()]
    packets = [json.loads(l) for l in lines]
    res1 = sum((i // 2) + 1 for i in range(0, len(packets), 2) if compare(packets[i], packets[i+1]) < 0)
    allp = packets + [[[2]], [[6]]]
    allp.sort(key=cmp_to_key(compare))
    res2 = (allp.index([[2]]) + 1) * (allp.index([[6]]) + 1)
    sys.stdout.write(f"{res1}\n{res2}\n")