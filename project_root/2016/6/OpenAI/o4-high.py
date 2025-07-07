import sys
with open(sys.argv[1]) as f:
    line = f.readline().rstrip('\n')
    if not line:
        sys.stdout.write(' ')
    else:
        m = len(line)
        counts = [dict() for _ in range(m)]
        for i, c in enumerate(line):
            counts[i][c] = 1
        for line in f:
            line = line.rstrip('\n')
            for i, c in enumerate(line):
                d = counts[i]
                d[c] = d.get(c, 0) + 1
        most = []
        least = []
        for d in counts:
            items = list(d.items())
            items.sort(key=lambda x: x[1], reverse=True)
            most.append(items[0][0])
            least.append(items[-1][0])
        sys.stdout.write(''.join(most) + ' ' + ''.join(least))