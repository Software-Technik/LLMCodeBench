import sys

def parse_and_compute(text):
    lines = text.strip().splitlines()
    H = len(lines); W = len(lines[0])
    ys = []; xs = []
    row_counts = [0]*H; col_counts = [0]*W
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c=='#':
                ys.append(i); xs.append(j)
                row_counts[i]+=1; col_counts[j]+=1
    empty_row = [1 if row_counts[i]==0 else 0 for i in range(H)]
    empty_col = [1 if col_counts[j]==0 else 0 for j in range(W)]
    prefix_row = [0]*(H+1)
    for i in range(H):
        prefix_row[i+1] = prefix_row[i] + empty_row[i]
    prefix_col = [0]*(W+1)
    for j in range(W):
        prefix_col[j+1] = prefix_col[j] + empty_col[j]
    def compute(exp):
        n = len(ys)
        new_y = [ys[k] + exp*prefix_row[ys[k]] for k in range(n)]
        new_x = [xs[k] + exp*prefix_col[xs[k]] for k in range(n)]
        new_y.sort(); new_x.sort()
        total = 0; s = 0
        for i,v in enumerate(new_y):
            total += v*i - s; s += v
        s = 0
        for i,v in enumerate(new_x):
            total += v*i - s; s += v
        return total
    return compute(1), compute(999999)

if __name__=="__main__":
    text = open(sys.argv[1]).read()
    a,b = parse_and_compute(text)
    sys.stdout.write(f"{a} {b}")