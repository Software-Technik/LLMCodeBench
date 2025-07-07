import sys
def main():
    data = open(sys.argv[1], "rb").read().strip()
    n = len(data)
    h = n >> 1
    r1 = r2 = 0
    first = data[0]
    for i in range(n - 1):
        x = data[i]
        if x == data[i + 1]:
            r1 += x - 48
        j = i + h
        if j >= n:
            j -= n
        if x == data[j]:
            r2 += x - 48
    x = data[-1]
    if x == first:
        r1 += x - 48
    j = h - 1
    if x == data[j]:
        r2 += x - 48
    print(r1)
    print(r2)
if __name__ == "__main__":
    main()