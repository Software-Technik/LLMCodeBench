import sys

count1 = count2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if not line: continue
        range_part, char_part, pw = line.split()
        lo, hi = map(int, range_part.split('-'))
        c = char_part[0]
        cnt = pw.count(c)
        if lo <= cnt <= hi:
            count1 += 1
        if (pw[lo-1] == c) ^ (pw[hi-1] == c):
            count2 += 1

print(count1, count2)