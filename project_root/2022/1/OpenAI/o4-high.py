import sys

def main():
    path = sys.argv[1]
    max1 = max2 = max3 = curr = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                curr += int(line)
            else:
                if curr > max1:
                    max3, max2, max1 = max2, max1, curr
                elif curr > max2:
                    max3, max2 = max2, curr
                elif curr > max3:
                    max3 = curr
                curr = 0
        if curr:
            if curr > max1:
                max3, max2, max1 = max2, max1, curr
            elif curr > max2:
                max3, max2 = max2, curr
            elif curr > max3:
                max3 = curr
    sys.stdout.write(f"{max1}\n{max1+max2+max3}\n")

if __name__ == "__main__":
    main()