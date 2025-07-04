import sys
from collections import defaultdict


def follows_rules(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i

    for a, b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0

    return True, update[len(update) // 2]


def part1(raw_rules, updates):
    ans = 0

    for update in updates:
        good, mid = follows_rules(update)
        if good:
            ans += mid

    return ans


def part2(raw_rules, updates):
    def follows_rules(update):
        idx = {}
        for i, num in enumerate(update):
            idx[num] = i

        for a, b in rules:
            if a in idx and b in idx and not idx[a] < idx[b]:
                return False, 0

        return True, update[len(update) // 2]

    def sort_correctly(update):
        while True:
            is_sorted = True
            for i in range(len(update) - 1):
                # Out of order?
                if (update[i + 1], update[i]) in rules:
                    is_sorted = False
                    update[i], update[i + 1] = update[i + 1], update[i]

            if is_sorted:
                return update

    ans = 0

    for update in updates:
        if follows_rules(update)[0]:
            continue

        seq = sort_correctly(update)
        ans += seq[len(seq) // 2]

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    raw_rules, updates = fin.read().strip().split("\n\n")
    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

    print(part1(raw_rules, updates), part2(raw_rules, updates))

