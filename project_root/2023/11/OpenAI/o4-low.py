import sys

def compute(positions, h, w, expansion_factor):
    n = len(positions)
    ys = [y for y,x in positions]
    xs = [x for y,x in positions]

    row_counts = [0]*h
    col_counts = [0]*w
    for y,x in positions:
        row_counts[y]+=1
        col_counts[x]+=1

    empty_row_prefix = [0]*(h+1)
    for i in range(h):
        empty_row_prefix[i+1] = empty_row_prefix[i] + (row_counts[i]==0)
    empty_col_prefix = [0]*(w+1)
    for i in range(w):
        empty_col_prefix[i+1] = empty_col_prefix[i] + (col_counts[i]==0)

    new_y = [y + expansion_factor*empty_row_prefix[y] for y in ys]
    new_x = [x + expansion_factor*empty_col_prefix[x] for x in xs]

    def sum_pair(arr):
        arr.sort()
        total = 0
        n = len(arr)
        for i,v in enumerate(arr):
            total += v*(2*i-n+1)
        return total

    return sum_pair(new_y) + sum_pair(new_x)

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = [line.rstrip() for line in f]
    h = len(lines)
    w = len(lines[0])
    positions = [(i,j) for i,row in enumerate(lines) for j,ch in enumerate(row) if ch=='#']
    p1 = compute(positions, h, w, 1)
    p2 = compute(positions, h, w, 999_999)
    print(p1, p2)

if __name__=='__main__':
    main()