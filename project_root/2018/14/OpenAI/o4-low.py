import sys

def compute():
    with open(sys.argv[1]) as f:
        text = f.read().strip()
    target = int(text)
    # Part 1
    scores = [3, 7]
    e1, e2 = 0, 1
    t1 = target + 10
    while len(scores) < t1:
        s = scores[e1] + scores[e2]
        if s >= 10:
            scores.append(s // 10)
        scores.append(s % 10)
        e1 = (e1 + scores[e1] + 1) % len(scores)
        e2 = (e2 + scores[e2] + 1) % len(scores)
    p1 = ''.join(str(i) for i in scores[target:target+10])
    # Part 2
    pattern = [int(c) for c in text]
    m = len(pattern)
    lps = [0] * m
    l = 0
    for i in range(1, m):
        while l > 0 and pattern[i] != pattern[l]:
            l = lps[l-1]
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
    scores = [3, 7]
    e1, e2, j, ans = 0, 1, 0, None
    while True:
        s = scores[e1] + scores[e2]
        for d in ((s//10, s%10) if s >= 10 else (s%10,)):
            scores.append(d)
            while j > 0 and d != pattern[j]:
                j = lps[j-1]
            if d == pattern[j]:
                j += 1
                if j == m:
                    ans = len(scores) - m
                    break
        if ans is not None:
            break
        e1 = (e1 + scores[e1] + 1) % len(scores)
        e2 = (e2 + scores[e2] + 1) % len(scores)
    sys.stdout.write(p1 + ' ' + str(ans))

if __name__ == '__main__':
    compute()