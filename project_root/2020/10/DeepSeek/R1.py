import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines = []

if not lines:
    print("0 1")
    sys.exit(0)

lines = [int(line.strip()) for line in lines if line.strip()]

srtd = sorted(lines)
arr = [0] + srtd + [srtd[-1] + 3]
ones = 0
threes = 0
for i in range(1, len(arr)):
    diff = arr[i] - arr[i-1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1
result1 = ones * threes

paths = {0: 1}
for s in srtd:
    paths[s] = paths.get(s-1, 0) + paths.get(s-2, 0) + paths.get(s-3, 0)
result2 = paths[srtd[-1]]

print(result1, result2)