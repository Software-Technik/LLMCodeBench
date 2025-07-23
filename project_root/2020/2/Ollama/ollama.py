import sys

input_path = sys.argv[1]
lines = [x.strip() for x in open(input_path)]
split = [x.split(' ') for x in lines]

def part1():
    valid_count = sum(1 for a,b,c in split if(int(a.split('-')[0]) <= c.count(b[0]) <= int(a.split('-')[1])))
    print(valid_count)

part1()

def part2():
    valid_count = 0
    for lo, ch, pw in [(a.split('-'), b[0], c) for a,b,c in split]:
        idx1 = int(lo[0]) - 1
        idx2 = int(lo[1]) - 1
        if bool(pw[idx1] == ch) ^ bool(pw[idx2] == ch):
            valid_count += 1
    print(valid_count)

part2()