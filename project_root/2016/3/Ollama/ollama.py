import sys

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

def parse_input(filename):
    with open(filename) as f:
        data = [list(map(int, line.split())) for line in f]
    vertical = list(zip(*data))
    return data, vertical

def part1(horizontal):
    return sum(is_triangle(row) for row in horizontal)

def part2(data_rows, num_cols):
    total = 0
    for col in range(num_cols - 2):
        for start_row in range(len(data_rows) - 2):
            if is_triangle([data_rows[start_row + i][col] for i in range(3)]):
                total += 1
    return total

if __name__ == "__main__":
    filename = sys.argv[1]
    horizontal, vertical = parse_input(filename)
    print(part1(horizontal), part2(vertical, len(horizontal)))