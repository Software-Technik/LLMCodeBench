import sys
from array import array

input_path = sys.argv[1]
with open(input_path) as f:
    data = f.read().strip()
initial = list(map(int, data.split(',')))
N1, N2 = 2020, 30000000
size = N2
arr = array('I', [0]) * (size + 1)
for i, num in enumerate(initial[:-1], start=1):
    arr[num] = i
last = initial[-1]
res1 = None
k = len(initial)
for turn in range(k + 1, N2 + 1):
    prev = arr[last]
    if prev == 0:
        curr = 0
    else:
        curr = (turn - 1) - prev
    arr[last] = turn - 1
    last = curr
    if turn == N1:
        res1 = last
print(res1, last)