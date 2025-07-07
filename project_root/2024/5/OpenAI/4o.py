import sys


def follows_rules(update, rules):
    idx = {num: i for i, num in enumerate(update)}
    return all(idx.get(a, -1) < idx.get(b, -1) for a, b in rules), update[len(update) // 2]


def part1(rules, updates):
    return sum(mid for update in updates if follows_rules(update, rules)[0])


def part2(rules, updates):
    def sort_correctly(update, rules):
        sorted_update = update[:]
        rules_set = set(rules)
        n = len(sorted_update)
        for _ in range(len(sorted_update) - 1):
            for i in range(n - 1):
                if (sorted_update[i + 1], sorted_update[i]) in rules_set:
                    sorted_update[i], sorted_update[i + 1] = sorted_update[i + 1], sorted_update[i]
        return sorted_update

    return sum(follows_rules(sort_correctly(update, rules), rules)[1] for update in updates)


input_path = sys.argv[1]
with open(input_path) as fin:
    raw_rules, updates = fin.read().strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in raw_rules.split("\n")]
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

    print(part1(rules, updates), part2(rules, updates))