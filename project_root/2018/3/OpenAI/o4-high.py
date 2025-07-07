import sys
from array import array

def main():
    lines = open(sys.argv[1]).read().strip().splitlines()
    claims = []
    label_to_index = {}
    max_x = max_y = 0
    for line in lines:
        parts = line.split()
        label = int(parts[0][1:])
        x_str,y_str = parts[2][:-1].split(',')
        w_str,h_str = parts[3].split('x')
        x = int(x_str); y = int(y_str); w = int(w_str); h = int(h_str)
        label_to_index[label] = len(claims)
        claims.append((label,x,y,w,h))
        xmax = x + w
        ymax = y + h
        if xmax > max_x: max_x = xmax
        if ymax > max_y: max_y = ymax
    W = max_x
    grid = array('i', [0]) * (max_x * max_y)
    claim_ok = [True] * len(claims)
    for label,x,y,w,h in claims:
        idx = label_to_index[label]
        for dy in range(h):
            base = (y+dy)*W + x
            for dx in range(w):
                pos = base + dx
                cur = grid[pos]
                if cur == 0:
                    grid[pos] = label
                elif cur > 0:
                    claim_ok[idx] = False
                    claim_ok[label_to_index[cur]] = False
                    grid[pos] = -1
                else:
                    claim_ok[idx] = False
    overlap = grid.count(-1)
    idx = claim_ok.index(True)
    sys.stdout.write(f"{overlap} {claims[idx][0]}")

if __name__ == "__main__":
    main()