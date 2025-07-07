from collections import deque
import sys

class Node:
    def __init__(self, n_children, n_metadata, parent):
        self.n_children = n_children
        self.parent = parent
        self.n_metadata = n_metadata
        self.children = []
        self.metadata = []

    @property
    def unprocessed_children(self):
        return self.n_children > len(self.children)

    @property
    def value(self):
        if self.children:
            return sum(self.children[i - 1].value for i in self.metadata if 0 < i <= self.n_children)
        else:
            return sum(self.metadata)

def main():
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = deque(map(int, f.read().strip().split()))

    tree = []
    parent = None
    checksum = 0

    while data:
        n_children = data.popleft()
        n_metadata = data.popleft()
        node = Node(n_children, n_metadata, parent)
        tree.append(node)
        if parent:
            parent.children.append(node)

        while not node.unprocessed_children:
            node.metadata = [data.popleft() for _ in range(node.n_metadata)]
            checksum += sum(node.metadata)
            if parent is None:
                break
            node = parent
            parent = node.parent

        if node.unprocessed_children:
            parent = node

    sys.stdout.write(f"{checksum} {tree[0].value}")

if __name__ == "__main__":
    main()