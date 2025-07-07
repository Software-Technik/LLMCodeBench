import sys
from functools import lru_cache

dirsums = ((3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1))

def part1(data):
    p1 = int(data[0].split()[-1])
    p2 = int(data[1].split()[-1])
    s1 = s2 = 0
    die = 1
    rolled = 0
    while True:
        r1 = die; die = die+1 if die<100 else 1
        r2 = die; die = die+1 if die<100 else 1
        r3 = die; die = die+1 if die<100 else 1
        rolled += 3
        s = r1 + r2 + r3
        p1 = (p1-1 + s) % 10 + 1
        s1 += p1
        if s1 >= 1000:
            return s2 * rolled
        r1 = die; die = die+1 if die<100 else 1
        r2 = die; die = die+1 if die<100 else 1
        r3 = die; die = die+1 if die<100 else 1
        rolled += 3
        s = r1 + r2 + r3
        p2 = (p2-1 + s) % 10 + 1
        s2 += p2
        if s2 >= 1000:
            return s1 * rolled

@lru_cache(None)
def cw(p1, p2, s1, s2, turn):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    w1 = w2 = 0
    for ds, freq in dirsums:
        if turn == 1:
            np1 = (p1-1 + ds) % 10 + 1
            t1, t2 = cw(np1, p2, s1 + np1, s2, 2)
        else:
            np2 = (p2-1 + ds) % 10 + 1
            t1, t2 = cw(p1, np2, s1, s2 + np2, 1)
        w1 += t1 * freq
        w2 += t2 * freq
    return (w1, w2)

def part2(data):
    p1 = int(data[0].split()[-1])
    p2 = int(data[1].split()[-1])
    return max(cw(p1, p2, 0, 0, 1))

data = open(sys.argv[1]).read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")