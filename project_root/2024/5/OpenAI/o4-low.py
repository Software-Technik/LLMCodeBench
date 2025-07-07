import sys

def main():
    with open(sys.argv[1]) as f:
        raw_rules, raw_updates = f.read().strip().split("\n\n")
    rules = []
    violation = set()
    for line in raw_rules.splitlines():
        a, b = map(int, line.split("|"))
        rules.append((a, b))
        violation.add((b, a))
    updates = [list(map(int, line.split(","))) for line in raw_updates.splitlines()]

    part1 = part2 = 0
    for upd in updates:
        idx = {num: i for i, num in enumerate(upd)}
        mid = upd[len(upd) // 2]
        ok = True
        for a, b in rules:
            if a in idx and b in idx and idx[a] >= idx[b]:
                ok = False
                break
        if ok:
            part1 += mid
            continue
        arr = upd
        n = len(arr)
        while True:
            swapped = False
            for i in range(n - 1):
                if (arr[i+1], arr[i]) in violation:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True
            if not swapped:
                break
        part2 += arr[n // 2]
    print(part1, part2)

if __name__ == "__main__":
    main()