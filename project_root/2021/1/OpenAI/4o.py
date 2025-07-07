def part1(data):
    return sum(int(data[i]) < int(data[i + 1]) for i in range(len(data) - 1))

def part2(data):
    return sum(int(data[i]) < int(data[i + 3]) for i in range(len(data) - 3))

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f if line.strip()]
    print(f"{part1(data)} {part2(data)}")