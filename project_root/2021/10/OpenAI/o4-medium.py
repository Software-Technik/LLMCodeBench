import sys
path = sys.argv[1]
closers = {')':'(', ']':'[', '}':'{', '>':'<'}
s1 = {')':3, ']':57, '}':1197, '>':25137}
s2 = {'(':1, '[':2, '{':3, '<':4}
total1 = 0
comp = []
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line: continue
        stack = []
        bad = False
        for c in line:
            if c in s2:
                stack.append(c)
            else:
                if not stack or stack[-1] != closers[c]:
                    total1 += s1[c]
                    bad = True
                    break
                stack.pop()
        if not bad:
            score = 0
            for c in reversed(stack):
                score = score*5 + s2[c]
            comp.append(score)
comp.sort()
mid = comp[len(comp)//2]
sys.stdout.write(f"{total1} {mid}")