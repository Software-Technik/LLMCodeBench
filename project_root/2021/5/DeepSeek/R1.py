import sys
import numpy as np

def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f if line.strip()]
    
    parsed_data = []
    max_val = 0
    for line in lines:
        parts = line.replace(' -> ', ',').split(',')
        coords = tuple(map(int, parts))
        parsed_data.append(coords)
        max_val = max(max_val, max(coords))
    size = max_val + 1

    diagram1 = np.zeros((size, size), dtype=int)
    for x1, y1, x2, y2 in parsed_data:
        if x1 == x2 or y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            diagram1[y1:y2+1, x1:x2+1] += 1
    part1_res = np.sum(diagram1 > 1)

    diagram2 = np.zeros((size, size), dtype=int)
    for x1, y1, x2, y2 in parsed_data:
        if x1 == x2 or y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            diagram2[y1:y2+1, x1:x2+1] += 1
        else:
            steps = abs(x1 - x2)
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            for i in range(steps + 1):
                diagram2[y1 + i * dy, x1 + i * dx] += 1
    part2_res = np.sum(diagram2 > 1)

    sys.stdout.write(f"{part1_res} {part2_res}")

if __name__ == "__main__":
    main()