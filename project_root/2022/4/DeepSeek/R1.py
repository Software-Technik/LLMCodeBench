import sys

def main():
    count1 = 0
    count2 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.replace('-', ',').split(',')
            a1, a2, b1, b2 = map(int, parts)
            if (a1 - b1) * (a2 - b2) <= 0:
                count1 += 1
            if max(a1, b1) <= min(a2, b2):
                count2 += 1
    sys.stdout.write(f"{count1}\n{count2}\n")

if __name__ == '__main__':
    main()