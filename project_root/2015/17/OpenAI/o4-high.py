import sys

def main():
    data = [int(line) for line in open(sys.argv[1])]
    target = 25 if len(data) == 5 else 150
    containers = sorted(data, reverse=True)
    total = 0
    min_count = len(containers) + 1
    min_ways = 0
    def dfs(i, s, c):
        nonlocal total, min_count, min_ways
        if s == target:
            total += 1
            if c < min_count:
                min_count = c
                min_ways = 1
            elif c == min_count:
                min_ways += 1
            return
        if s > target or i == len(containers):
            return
        dfs(i + 1, s + containers[i], c + 1)
        dfs(i + 1, s, c)
    dfs(0, 0, 0)
    sys.stdout.write(f"{total}\n{min_ways}\n")

if __name__ == '__main__':
    main()