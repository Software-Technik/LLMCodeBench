import sys

r1 = r2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        a, b = line.split(',')
        s1_0, s1_1 = map(int, a.split('-'))
        s2_0, s2_1 = map(int, b.split('-'))
        if (s1_0 - s2_0) * (s1_1 - s2_1) <= 0:
            r1 += 1
        if s1_1 >= s2_0 and s2_1 >= s1_0:
            r2 += 1

sys.stdout.write(f"{r1}\n{r2}\n")