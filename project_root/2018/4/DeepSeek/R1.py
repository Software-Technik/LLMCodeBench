import sys
from datetime import datetime
from collections import defaultdict

logs = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        time_str = line[1:17]
        action = line[19:]
        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        logs.append((dt, action))

logs.sort(key=lambda x: x[0])

guard_info = defaultdict(lambda: {'total': 0, 'minutes': [0]*60})
current_guard = None
sleep_start = None

for dt, action in logs:
    if action.startswith('Guard'):
        parts = action.split()
        guard_id = int(parts[1][1:])
        current_guard = guard_id
        sleep_start = None
    elif action == 'falls asleep':
        if current_guard is not None:
            sleep_start = dt.minute
    elif action == 'wakes up':
        if current_guard is not None and sleep_start is not None:
            wake_minute = dt.minute
            duration = wake_minute - sleep_start
            guard_info[current_guard]['total'] += duration
            for m in range(sleep_start, wake_minute):
                guard_info[current_guard]['minutes'][m] += 1
            sleep_start = None

best_guard1 = None
max_total = -1
for guard, info in guard_info.items():
    if info['total'] > max_total:
        max_total = info['total']
        best_guard1 = guard

best_minute1 = -1
max_count1 = -1
for minute, count in enumerate(guard_info[best_guard1]['minutes']):
    if count > max_count1:
        max_count1 = count
        best_minute1 = minute

best_guard2 = None
best_minute2 = -1
max_count2 = -1
for guard, info in guard_info.items():
    for minute, count in enumerate(info['minutes']):
        if count > max_count2:
            max_count2 = count
            best_guard2 = guard
            best_minute2 = minute

sys.stdout.write(f"{best_guard1 * best_minute1} {best_guard2 * best_minute2}")