import sys

with open(sys.argv[1]) as f:
    data = map(int, f.read().split())
stack = []
checksum = 0
c = next(data); m = next(data)
stack.append([c, m, []])
root_value = 0
while stack:
    rem, n_meta, child_vals = stack[-1]
    if rem:
        stack[-1][0] = rem - 1
        c = next(data); m = next(data)
        stack.append([c, m, []])
    else:
        stack.pop()
        meta = [next(data) for _ in range(n_meta)]
        checksum += sum(meta)
        if child_vals:
            val = 0
            for idx in meta:
                if 1 <= idx <= len(child_vals):
                    val += child_vals[idx-1]
        else:
            val = sum(meta)
        if stack:
            stack[-1][2].append(val)
        else:
            root_value = val
print(f"{checksum} {root_value}")