import sys

data = open(sys.argv[1]).read().splitlines()
n = len(data[0])
counts = [[0]*26 for _ in range(n)]
for line in data:
    for i, c in enumerate(line):
        counts[i][ord(c)-97] += 1
first = []
second = []
for col in counts:
    mx = -1; mxc = 0
    mn = 10**18; mnc = 0
    for j, v in enumerate(col):
        if v > mx:
            mx = v; mxc = j
        if v > 0 and v < mn:
            mn = v; mnc = j
    first.append(chr(mxc+97))
    second.append(chr(mnc+97))
sys.stdout.write(''.join(first) + ' ' + ''.join(second))