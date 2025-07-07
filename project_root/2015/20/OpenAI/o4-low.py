import sys
def main():
    target = int(open(sys.argv[1]).read().strip())
    n1 = target // 10
    p1 = [0] * (n1 + 1)
    for i in range(1, n1 + 1):
        mul = i * 10
        for j in range(i, n1 + 1, i):
            p1[j] += mul
    for i in range(1, n1 + 1):
        if p1[i] >= target:
            ans1 = i
            break
    n2 = target // 11
    p2 = [0] * (n2 + 1)
    for i in range(1, n2 + 1):
        mul = i * 11
        cnt = 0
        for j in range(i, n2 + 1, i):
            p2[j] += mul
            cnt += 1
            if cnt == 50:
                break
    for i in range(1, n2 + 1):
        if p2[i] >= target:
            ans2 = i
            break
    sys.stdout.write(f"{ans1}\n{ans2}\n")

if __name__ == "__main__":
    main()