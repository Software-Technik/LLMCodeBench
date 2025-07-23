import sys

with open(sys.argv[1]) as f:
    data_list = list(map(int, f.read().split()))

stack = []
index = 0
total_checksum = 0
root_value = None

while index < len(data_list) or stack:
    if stack and stack[-1][0] == 0:
        node = stack.pop()
        rem_children, n_meta, children_vals = node
        meta = data_list[index:index+n_meta]
        index += n_meta
        total_checksum += sum(meta)
        if children_vals:
            node_value = 0
            for m in meta:
                if 1 <= m <= len(children_vals):
                    node_value += children_vals[m-1]
        else:
            node_value = sum(meta)
        if stack:
            stack[-1][2].append(node_value)
            stack[-1][0] -= 1
        else:
            root_value = node_value
    else:
        if index + 1 >= len(data_list):
            break
        n_children = data_list[index]
        n_meta = data_list[index+1]
        index += 2
        stack.append([n_children, n_meta, []])

sys.stdout.write(f"{total_checksum} {root_value}")