import sys

def parse_input(text):
    return [list(line) for line in text.strip().splitlines()]

def compute(data, expansion_factor):
    y, x = zip(*[(i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val == "#"])
    y, x = list(y), list(x)
    
    empty_r = [i for i, row in enumerate(data) if all(val == "." for val in row)]
    empty_c = [i for i in range(len(data[0])) if all(data[r][i] == "." for r in range(len(data)))]

    y_diff = sum(expansion_factor for r in empty_r if any(y_i > r for y_i in y))
    x_diff = sum(expansion_factor for c in empty_c if any(x_i > c for x_i in x))

    new_y = [y_i + y_diff for y_i in y]
    new_x = [x_i + x_diff for x_i in x]

    total_distance = sum(abs(new_y[i] - new_y[j]) + abs(new_x[i] - new_x[j]) for i in range(len(new_y)) for j in range(i+1, len(new_y)))

    return total_distance

def part1(text):
    data = parse_input(text)
    return compute(data, expansion_factor=1)

def part2(text):
    data = parse_input(text)
    return compute(data, expansion_factor=999_999)

input_file = sys.argv[1]
with open(input_file) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")