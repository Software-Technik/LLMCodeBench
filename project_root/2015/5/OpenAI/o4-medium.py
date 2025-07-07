import sys

def main():
    data = open(sys.argv[1]).read().splitlines()
    p1 = p2 = 0
    vowels = set("aeiou")
    for s in data:
        vc = 0
        hd = False
        hb = False
        prev = ''
        for c in s:
            if c in vowels: vc += 1
            if prev:
                if prev == c: hd = True
                if prev + c in ("ab","cd","pq","xy"):
                    hb = True
                    break
            prev = c
        if vc >= 3 and hd and not hb:
            p1 += 1
        hp = False
        hr = False
        pairs = {}
        for i in range(len(s)):
            if i >= 2 and s[i] == s[i-2]:
                hr = True
            if i+1 < len(s):
                pair = s[i:i+2]
                if pair in pairs:
                    if pairs[pair] < i-1:
                        hp = True
                else:
                    pairs[pair] = i
            if hp and hr:
                break
        if hp and hr:
            p2 += 1
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == "__main__":
    main()