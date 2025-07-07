import sys
from datetime import datetime
from collections import defaultdict

def main():
    with open(sys.argv[1]) as f:
        lines = [line.rstrip() for line in f]
    logs = []
    for line in lines:
        ts = datetime.strptime(line[:18], "[%Y-%m-%d %H:%M]")
        action = line[19:]
        logs.append((ts, action))
    logs.sort(key=lambda x: x[0])
    guard_totals = defaultdict(int)
    guard_minutes = defaultdict(lambda: [0]*60)
    current_guard = None
    asleep_min = None
    for ts, action in logs:
        if action.startswith("Guard"):
            current_guard = int(action.split()[1][1:])
        elif action == "falls asleep":
            asleep_min = ts.minute
        else:  # wakes up
            for m in range(asleep_min, ts.minute):
                guard_totals[current_guard] += 1
                guard_minutes[current_guard][m] += 1
    # Part 1
    g1 = max(guard_totals, key=lambda g: guard_totals[g])
    m1 = guard_minutes[g1].index(max(guard_minutes[g1]))
    # Part 2
    best = (None, None, -1)
    for g, minutes in guard_minutes.items():
        for m, cnt in enumerate(minutes):
            if cnt > best[2]:
                best = (g, m, cnt)
    g2, m2, _ = best
    print(g1 * m1, g2 * m2)

if __name__ == "__main__":
    main()