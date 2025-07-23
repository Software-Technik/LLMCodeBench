from collections import deque

class Node:
    def __init__(self, n_children, n_metadata):
        self.n_children = n_children
        self.children = []
        self.metadata: list[int] = []

    @property
    def is_header(self):
        return not len(self.children) < self.n_children

    @property
    def value(self):
        if self.children:
            return sum((self.children[i - 1].value for i in self.metadata if i <= len(self.children)), 0)
        else:
            return sum(self.metadata)

inout_strings = 'input.txt'
with open(inout_strings) as f:
    data = deque(int(x) for x in f.read().split())

tree: list[Node] = []
checksum, total_sum = 0, 0
current: Node | None = None

while data:
    if current is None or not current.is_header:
        n_children = data.popleft()
        n_metadata = data.popleft()
        node = Node(n_children, n_metadata)
        tree.append(node)
        if current:
            current.children.append(node)
        else:
            total_sum += sum(data.popleft() for _ in range(3))

    is_complete = len(node.children) + 1 > node.n_children

    if not data or (is_complete and node.metadata):
        metadata_length = node.n_metadata
        if node.is_header:
            node.metadata.extend(map(int, node.metadata))

    checksum += sum(data.popleft() for _ in range(min(metadata_length, len(node.children))))
    current = tree[-1]  # Assign parent reference

sys.stdout.write(f"{checksum} {tree[0].value}")