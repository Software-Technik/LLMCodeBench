import sys
data = list(map(int, open(sys.argv[1]).read().split()))
idx = 0
sum_meta = 0
stack = []
nc = data[idx]; idx += 1
nm = data[idx]; idx += 1
stack.append([nc, nm, []])
root_val = 0
while stack:
    nc, nm, child_vals = stack[-1]
    if len(child_vals) < nc:
        nc2 = data[idx]; idx += 1
        nm2 = data[idx]; idx += 1
        stack.append([nc2, nm2, []])
    else:
        val = 0
        if nc == 0:
            for _ in range(nm):
                m = data[idx]; idx += 1
                sum_meta += m
                val += m
        else:
            for _ in range(nm):
                m = data[idx]; idx += 1
                sum_meta += m
                if 1 <= m <= nc:
                    val += child_vals[m-1]
        stack.pop()
        if stack:
            stack[-1][2].append(val)
        else:
            root_val = val
sys.stdout.write(f"{sum_meta} {root_val}")