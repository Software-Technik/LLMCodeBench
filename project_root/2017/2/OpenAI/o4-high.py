import sys
def main(path):
    p1 = 0
    p2 = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            row = list(map(int, line.split()))
            p1 += max(row) - min(row)
            row.sort(reverse=True)
            for i in range(len(row) - 1):
                a = row[i]
                for j in range(i + 1, len(row)):
                    b = row[j]
                    if a % b == 0:
                        p2 += a // b
                        break
                else:
                    continue
                break
    sys.stdout.write(f"{p1}\n{p2}\n")
if __name__ == "__main__":
    main(sys.argv[1])