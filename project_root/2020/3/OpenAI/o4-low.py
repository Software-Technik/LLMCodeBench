import sys

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = [line.strip() for line in f]
    height = len(lines)
    width = len(lines[0])
    def count(dx, dy):
        x = y = c = 0
        while y + dy < height:
            x = (x + dx) % width
            y += dy
            if lines[y][x] == "#":
                c += 1
        return c
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    r1 = count(3,1)
    tot = 1
    for dx, dy in slopes:
        tot *= count(dx, dy)
    print(f"{r1} {tot}")

if __name__ == "__main__":
    main()