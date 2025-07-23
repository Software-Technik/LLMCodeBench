import sys
from collections import defaultdict


def follows_rules(update, rules):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i

    for a, b in rules:
        if a in idx and b in idx and idx[a] >= idx[b]:
            return False, 0

    return True, update[len(update) // 2]


def part1(rules, updates):
    ans = 0

    for update in updates:
        good, mid = follows_rules(update, rules)
        if good:
            ans += mid

    return ans


def part2(rules, updates):
    rules_set = set(rules)

    def sort_correctly(update):
        changed = True
        while changed:
            changed = False
            for i in range(len(update) - 1):
                if (update[i + 1], update[i]) in rules_set:
                    update[i], update[i + 1] = update[i + 1], update[i]
                    changed = True
        return update

    ans = 0

    for update in updates:
        if follows_rules(update, rules)[0]:
            continue

        seq = sort_correctly(update.copy())
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

    print(part1(rules, updates), part2(rules, updates))