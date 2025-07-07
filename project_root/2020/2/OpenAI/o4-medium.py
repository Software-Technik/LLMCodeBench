import sys

res1 = res2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        low_high, char_colon, pwd = line.split()
        low, high = map(int, low_high.split('-'))
        c = char_colon[0]
        cnt = pwd.count(c)
        if low <= cnt <= high:
            res1 += 1
        p1 = pwd[low-1] == c
        p2 = pwd[high-1] == c
        if p1 ^ p2:
            res2 += 1
print(res1, res2)