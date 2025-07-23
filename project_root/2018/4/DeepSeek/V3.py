from datetime import datetime
from collections import namedtuple, defaultdict
import numpy as np
import sys

def get_shift(log):
    ilog = iter(log)
    guard = int(next(ilog).action[7:].strip().split()[0])
    shift_log = np.zeros(60, dtype=np.int8)
    sleep = 0
    for entry in ilog:
        if entry.action.startswith("Guard"):
            yield guard, shift_log
            shift_log = np.zeros(60, dtype=np.int8)
            guard = int(entry.action[7:].strip().split()[0])
            continue
        if entry.action == "falls asleep":
            sleep = entry.dt.minute
        else:
            wakes = entry.dt.minute
            shift_log[sleep:wakes] = 1
    yield guard, shift_log

Log = namedtuple("Log", ["dt", "action"])

timelog = []
with open(sys.argv[1]) as f:
    for line in f:
        time = datetime.strptime(line[:18], "[%Y-%m-%d %H:%M]")
        action = line.strip()[19:]
        timelog.append(Log(time, action))

timelog.sort(key=lambda x: x.dt)

guards = defaultdict(list)
for guard, shift_log in get_shift(timelog):
    guards[guard].append(shift_log)

totals = []
for guard, shifts in guards.items():
    all_shifts = np.array(shifts)
    total = all_shifts.sum()
    minute_sum = all_shifts.sum(axis=0)
    totals.append((guard, total, minute_sum))

part1 = max(totals, key=lambda x: x[1])
part2 = max(totals, key=lambda x: x[2].max())

sys.stdout.write(f"{part1[0]*part1[2].argmax()} {part2[0]*part2[2].argmax()}")