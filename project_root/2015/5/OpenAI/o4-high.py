import sys
vowels = set('aeiou')
forbids = {'ab','cd','pq','xy'}
c1 = c2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        s = line.strip()
        v = 0; d = False; bad = False
        for i,ch in enumerate(s):
            if ch in vowels: v += 1
            if i and ch == s[i-1]: d = True
            if i and s[i-1:i+1] in forbids:
                bad = True
                break
        if v >= 3 and d and not bad: c1 += 1
        p = {}; rep = False; pr = False; n = len(s)
        for i in range(n):
            if i+2 < n and s[i] == s[i+2]: rep = True
            if i+1 < n:
                pair = s[i:i+2]
                if pair in p:
                    if i - p[pair] > 1: pr = True
                else:
                    p[pair] = i
            if rep and pr: break
        if rep and pr: c2 += 1
print(c1, c2, sep="\n")