import sys

def main():
    data = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    pairs = {')':'(',']':'[','}':'{','>':'<'}
    err_score = {')':3,']':57,'}':1197,'>':25137}
    comp_score = {'(':1,'[':2,'{':3,'<':4}
    p1 = 0
    p2_scores = []
    for line in data:
        stack = []
        corrupt = False
        for c in line:
            if c in pairs.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != pairs[c]:
                    p1 += err_score[c]
                    corrupt = True
                    break
        if not corrupt:
            score = 0
            for c in reversed(stack):
                score = score*5 + comp_score[c]
            p2_scores.append(score)
    p2_scores.sort()
    m = p2_scores[len(p2_scores)//2]
    print(p1, m)

if __name__ == '__main__':
    main()