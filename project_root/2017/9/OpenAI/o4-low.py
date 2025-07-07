import sys

def main():
    with open(sys.argv[1]) as f:
        s = f.read().strip()
    n = len(s)
    i = 0
    score = 0
    level = 0
    garbage = 0
    while i < n:
        c = s[i]
        if c == '<':
            i += 1
            while s[i] != '>':
                if s[i] == '!':
                    i += 2
                else:
                    garbage += 1
                    i += 1
        else:
            if c == '{':
                level += 1
            elif c == '}':
                score += level
                level -= 1
            i += 1
    print(score)
    print(garbage)

if __name__ == '__main__':
    main()