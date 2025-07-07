import sys

def binomial_row(n):
    row = [1] * (n + 1)
    for k in range(1, n // 2 + 1):
        row[k] = row[n - k] = row[k - 1] * (n - k + 1) // k
    return row

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = f.read().split()
    it = iter(lines)
    first = int(next(it))
    row_len = 1
    while True:
        try:
            for _ in range(row_len - 1):
                next(it)
            break
        except StopIteration:
            row_len += 1
            it = iter(lines)
            next(it)
    n = row_len
    values = binomial_row(n)
    sum1 = sum2 = 0
    idx = 0
    total_vals = len(lines)
    while idx < total_vals:
        line = list(map(int, lines[idx:idx + n]))
        idx += n
        add1 = add2 = (n & 1) == 1
        for a, b in zip(line, values):
            prod = a * b
            sum1 += prod if add1 else -prod
            add1 = not add1
        for a, b in zip(reversed(line), values):
            prod = a * b
            sum2 += prod if add2 else -prod
            add2 = not add2
    sys.stdout.write(f"{sum1} {sum2}")

if __name__ == "__main__":
    main()