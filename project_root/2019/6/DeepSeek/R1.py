import sys
import collections

def part1(children):
    total = 0
    node_depth = {}
    queue = collections.deque()
    queue.append(('COM',0))
    node_depth['COM'] = 0
    while queue:
        node, depth = queue.popleft()
        total += depth
        if node in children:
            for child in children[node]:
                node_depth[child] = depth + 1
                queue.append((child, depth + 1))
    return total, node_depth

def part2(parent_of, node_depth):
    A = parent_of['YOU']
    B = parent_of['SAN']
    da = node_depth[A]
    db = node_depth[B]
    curA = A
    curB = B
    if da > db:
        for _ in range(da - db):
            curA = parent_of[curA]
    else:
        for _ in range(db - da):
            curB = parent_of[curB]
    while curA != curB:
        curA = parent_of[curA]
        curB = parent_of[curB]
    lca = curA
    return da + db - 2 * node_depth[lca]

if __name__ == '__main__':
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read().splitlines()
    children = {}
    parent_of = {}
    for line in data:
        a, b = line.split(')')
        children.setdefault(a, []).append(b)
        parent_of[b] = a
    p1, node_depth = part1(children)
    p2 = part2(parent_of, node_depth)
    sys.stdout.write(f"{p1} {p2}")