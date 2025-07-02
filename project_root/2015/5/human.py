import sys

def part1(data):
    apply_rule1 = [i for i in data if sum(1 for c in i if c in "aeiou") > 2]
    apply_rule2 = [i for i in apply_rule1 if sum(1 if c == d else 0 for c, d in zip(i, i[1:])) > 0]
    apply_rule3 = [i for i in apply_rule2 if sum(1 if c + d in ["ab", "cd", "pq", "xy"] else 0 for c, d in zip(i, i[1:])) < 1]
    return len(apply_rule3)

def part2(data):
    apply_rule1 = [i for i in data if sum(1 if i.count(c + d) > 1 else 0 for c, d in zip(i, i[1:])) > 0]
    apply_rule2 = [i for i in apply_rule1 if sum(1 if c == d else 0 for c, d in zip(i, i[2:])) > 0]
    return len(apply_rule2)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")