import sys

with open(sys.argv[1]) as f:
    data = [int(line) for line in f]
frequency = sum(data)
seen = {0}
current = 0
n = len(data)
i = 0
while True:
    current += data[i]
    if current in seen:
        break
    seen.add(current)
    i += 1
    if i == n:
        i = 0
sys.stdout.write(f"{frequency} {current}")