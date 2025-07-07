import sys

def part1(text):
    total = 0
    for line in text.splitlines():
        a,b = line.split(":",1)[1].split("|",1)
        s1 = set(a.split()); s2 = set(b.split())
        c = len(s1 & s2)
        if c: total += 1 << (c-1)
    return total

def part2(text):
    cards = []
    for line in text.splitlines():
        a,b = line.split(":",1)[1].split("|",1)
        cards.append(len(set(a.split()) & set(b.split())))
    n = len(cards)
    dp = [0]*(n+1)
    pref = [0]*(n+2)
    for i in range(n-1, -1, -1):
        k = cards[i]
        end = i+k+1
        if end > n: end = n
        dp[i] = k + (pref[i+1] - pref[end])
        pref[i] = pref[i+1] + dp[i]
    return pref[0] + n

text = open(sys.argv[1]).read()
sys.stdout.write(f"{part1(text)} {part2(text)}")