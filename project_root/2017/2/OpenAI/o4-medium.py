import sys
total1 = total2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        if line.strip():
            row = list(map(int, line.split()))
            total1 += max(row) - min(row)
            row.sort(reverse=True)
            for i,a in enumerate(row):
                for b in row[i+1:]:
                    if a % b == 0:
                        total2 += a//b
                        break
                else:
                    continue
                break
print(total1)
print(total2)