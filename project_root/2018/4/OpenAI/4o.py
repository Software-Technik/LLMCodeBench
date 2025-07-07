from datetime import datetime
from collections import defaultdict, namedtuple
import sys

def get_shift(log):
    shift_log = [0] * 60
    current_guard = None
    sleep = 0

    for entry in log:
        if entry.action.startswith("Guard"):
            if current_guard is not None:
                yield current_guard, shift_log
            current_guard = int(entry.action.split()[1][1:])
            shift_log = [0] * 60
        elif entry.action == "falls asleep":
            sleep = entry.dt.minute
        elif entry.action == "wakes up":
            for minute in range(sleep, entry.dt.minute):
                shift_log[minute] += 1
    yield current_guard, shift_log

Log = namedtuple("Log", ["dt", "action"])
Total = namedtuple("Total", ["guard", "total", "minute_sum"])

timelog = []

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().strip().splitlines()

for entry in data:
    time = datetime.strptime(entry[:18], "[%Y-%m-%d %H:%M]")
    action = entry[19:]
    timelog.append(Log(time, action))

timelog.sort(key=lambda x: x.dt)

guards = defaultdict(lambda: [0] * 60)
for guard, shift_log in get_shift(timelog):
    guards[guard] = [x + y for x, y in zip(guards[guard], shift_log)]

totals = [
    Total(guard, sum(minute_sum), minute_sum)
    for guard, minute_sum in guards.items()
]

part1 = max(totals, key=lambda x: x.total)
part2 = max(totals, key=lambda x: max(x.minute_sum))

sys.stdout.write(f"{part1.guard * part1.minute_sum.index(max(part1.minute_sum))} {part2.guard * part2.minute_sum.index(max(part2.minute_sum))}")