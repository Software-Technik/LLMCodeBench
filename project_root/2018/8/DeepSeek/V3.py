from collections import deque
import sys

class Node:
    __slots__ = ('n_children', 'parent', 'n_metadata', 'children', 'metadata')
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
        if not self.children:
            return sum(self.metadata)
        return sum(self.children[i-1].value for i in self.metadata if 0 < i <= len(self.children))


def main():
    with open(sys.argv[1]) as f:
        data = deque(map(int, f.read().split()))

    tree = []
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
            node.metadata = [data.popleft() for _ in range(node.n_metadata)]
            checksum += sum(node.metadata)
            if parent is None:
                header = True
                continue
            node = parent
            parent = node.parent
            header = False

    sys.stdout.write(f"{checksum} {tree[0].value}")

if __name__ == "__main__":
    main()