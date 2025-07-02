import sys
from collections import Counter

def part1(data):
    template = data[0]
    rules = {a: b for a, b in [x.split(" -> ") for x in data[2:]]}

    for _ in range(10):
        new = ""
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            new += pair[0]
            if pair in rules:
                new += rules[pair]
        new += template[-1]
        template = new

    count = Counter(template).most_common()
    return count[0][1] - count[-1][1]

def part2(data):
    template = data[0]
    rules = {a: b for a, b in [x.split(" -> ") for x in data[2:]]}

    # Count each pair of letters in the template
    pairs = Counter([template[i : i + 2] for i in range(len(template) - 1)])

    # Update pairs count at each step as per rules
    for _ in range(40):
        new_pairs = Counter()
        for p, v in pairs.items():
            if p in rules:
                c = rules[p]
                new_pairs[p[0] + c] += v
                new_pairs[c + p[1]] += v
            else:
                new_pairs[p] += pairs[p]
        pairs = new_pairs

    # Count letters at the final step by counting first letter of each pairs,
    # plus the final letter which is invariant during the whole process
    count = Counter()
    for p, v in pairs.items():
        count[p[0]] += v
    count[template[-1]] += 1

    return count.most_common()[0][1] - count.most_common()[-1][1]

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")