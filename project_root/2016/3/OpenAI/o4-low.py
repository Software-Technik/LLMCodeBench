import sys

data = [list(map(int, line.split())) for line in open(sys.argv[1])]
p1 = 0
for x, y, z in data:
    s = x + y + z
    m = x if x > y and x > z else (y if y > z else z)
    if s - m > m:
        p1 += 1
p2 = 0
for i in range(0, len(data), 3):
    a, b, c = data[i], data[i+1], data[i+2]
    for j in range(3):
        x, y, z = a[j], b[j], c[j]
        s = x + y + z
        m = x if x > y and x > z else (y if y > z else z)
        if s - m > m:
            p2 += 1
sys.stdout.write(f"{p1} {p2}")