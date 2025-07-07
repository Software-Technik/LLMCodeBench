import sys
from collections import defaultdict
lines = open(sys.argv[1]).read().splitlines()
lines.sort()
sleep_totals = defaultdict(int)
sleep_minutes = defaultdict(lambda: [0]*60)
guard = asleep = None
for line in lines:
    minute = int(line[15:17])
    action = line[19:]
    if action[0] == 'G':
        guard = int(action.split()[1][1:])
    elif action[0] == 'f':
        asleep = minute
    else:
        for m in range(asleep, minute):
            sleep_totals[guard] += 1
            sleep_minutes[guard][m] += 1
g1 = max(sleep_totals, key=sleep_totals.get)
m1 = max(range(60), key=lambda m: sleep_minutes[g1][m])
g2 = m2 = c2 = 0
for g, mins in sleep_minutes.items():
    for m, cnt in enumerate(mins):
        if cnt > c2:
            c2 = cnt; g2 = g; m2 = m
sys.stdout.write(f"{g1*m1} {g2*m2}")