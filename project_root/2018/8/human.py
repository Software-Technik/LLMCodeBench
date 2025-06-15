from collections import deque
import sys

class Node:
    def __init__(self, n_children, n_metadata, parent):
        self.n_children = n_children
        self.parent = parent
        self.n_metadata = n_metadata
        self.children = list()
        self.metadata: list

    @property
    def unprocessed_children(self):
        return bool(self.n_children - len(self.children))

    def __len__(self):
        return len(self.children)

    def __lt__(self, other):
        return len(self) < len(other)

    @property
    def value(self):
        if self.children:
            return sum(self.children[i-1].value for i in self.metadata
                       if (i-1) < self.n_children)
        else:
            return sum(self.metadata)



inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = deque(int(x) for x in f.read().strip().split())


tree = list()
header = True
parent = None
checksum = 0

while data:
    if header:
        n_children = data.popleft()
        n_metadata = data.popleft()
        node = Node(n_children, n_metadata, parent)
        tree.append(node)
        if parent is not None:
            parent.children.append(node)

    if node.unprocessed_children:
        parent = node
        header = True
    else:
        node.metadata = [data.popleft() for i in range(node.n_metadata)]
        checksum += sum(node.metadata)
        if parent is None:
            header = True
            continue
        node = parent
        parent = node.parent
        header = False


print(checksum)
print(tree[0].value)