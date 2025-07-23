import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()
    T0 = int(data[0])
    limit = 1000000

    arr1 = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            arr1[j] += i

    n1 = 1
    while n1 <= limit:
        if 10 * arr1[n1] >= T0:
            break
        n1 += 1

    arr2 = [0] * (limit + 1)
    for i in range(1, limit + 1):
        end = 50 * i
        if end > limit:
            end = limit
        for j in range(i, end + 1, i):
            arr2[j] += 11 * i

    n2 = 1
    while n2 <= limit:
        if arr2[n2] >= T0:
            break
        n2 += 1

    print(n1)
    print(n2)

if __name__ == '__main__':
    main()