import sys

data = list(map(int, open(sys.argv[1]).read().split()))
i = 0
stack = []
checksum = 0
root_value = 0

while True:
    if stack and stack[-1][0] == 0:
        rem_c, n_meta, child_vals = stack.pop()
        meta = data[i:i+n_meta]; i += n_meta
        checksum += sum(meta)
        if child_vals:
            value = sum(child_vals[m-1] for m in meta if 1 <= m <= len(child_vals))
        else:
            value = sum(meta)
        if stack:
            stack[-1][2].append(value)
            stack[-1][0] -= 1
            continue
        else:
            root_value = value
            break
    else:
        n_c = data[i]; n_meta = data[i+1]; i += 2
        stack.append([n_c, n_meta, []])

sys.stdout.write(f"{checksum} {root_value}")