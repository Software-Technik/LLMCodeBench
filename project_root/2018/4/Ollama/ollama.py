from datetime import datetime
import numpy as np
import sys

def get_shift(log):
    ilog = iter(log)
    guard = int(next(ilog).action[7:].strip().split(" ")[0])
    shift_log = np.zeros(60, dtype="int")
    for entry in ilog:
        if entry.action.startswith("Guard"):
            yield guard, shift_log
            shift_log = np.zeros(60)
            guard = int(entry.action[7:].strip().split(" ")[0])
            continue
        if entry.action == "falls asleep":
            sleep = entry.dt.minute
        else:
            wakes = entry.dt.minute
            shift_log[sleep:wakes] += 1
    yield guard, shift_log

Log = namedtuple("Log", ["dt", "action"])
Total = namedtuple("Total", ["guard", "total", "minute_sum"])

timelog = []

inout_strings = sys.argv[1]
data_lines = open(inout_strings).read().strip().splitlines()

for entry in data_lines:
    time = datetime.strptime(entry[:18], "[%Y-%m-%d %H:%M]")
    action = entry.strip()[19:]
    timelog.append(Log(time, action))

timelog.sort(key=lambda x: x.dt)

guards = {}
for guard, shift_log in get_shift(timelog):
    guards.setdefault(guard, []).append(shift_log)

totals = [Total(guard, np.concatenate(shifts).sum(), np.concatenate(shifts).reshape(-1, 60).sum(axis=0)) for guard, shifts in guards.items()]

part1 = max(totals, key=lambda x: x.total)
part2 = max(totals, key=lambda x: x.minute_sum.max())

sys.stdout.write(f"{part1.guard*part1.minute_sum.argmax()} {part2.guard*part2.minute_sum.argmax()}")