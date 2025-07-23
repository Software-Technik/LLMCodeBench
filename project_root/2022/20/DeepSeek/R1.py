import sys

class Node:
    __slots__ = ('value', 'prev', 'next')
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def create_linked_list(data):
    nodes = []
    prev = None
    head = None
    zero_node = None
    for num in data:
        node = Node(num)
        nodes.append(node)
        if num == 0:
            zero_node = node
        if prev is not None:
            prev.next = node
            node.prev = prev
        else:
            head = node
        prev = node
    if head:
        head.prev = prev
        prev.next = head
    return nodes, zero_node

def mix(nodes, times):
    n_total = len(nodes)
    if n_total == 0:
        return
    for _ in range(times):
        for node in nodes:
            prev_node = node.prev
            next_node = node.next
            if prev_node == next_node:
                continue
            prev_node.next = next_node
            next_node.prev = prev_node
            if n_total == 1:
                moves = 0
            else:
                moves = node.value % (n_total - 1)
            if moves == 0:
                prev_node.next = node
                node.prev = prev_node
                node.next = next_node
                next_node.prev = node
            else:
                if moves > (n_total - 1) // 2:
                    moves = (n_total - 1) - moves
                    current = next_node
                    for _ in range(moves):
                        current = current.prev
                else:
                    current = next_node
                    for _ in range(moves):
                        current = current.next
                prev_current = current.prev
                prev_current.next = node
                node.prev = prev_current
                node.next = current
                current.prev = node

def get_grove_coordinates(zero_node, n_total):
    current = zero_node
    total = 0
    for step in [1000, 2000, 3000]:
        steps = step % n_total
        for _ in range(steps):
            current = current.next
        total += current.value
    return total

def main():
    with open(sys.argv[1]) as f:
        data = [int(line.strip()) for line in f]
    
    nodes1, zero1 = create_linked_list(data)
    n_total = len(nodes1)
    mix(nodes1, 1)
    ans1 = get_grove_coordinates(zero1, n_total)
    
    key = 811589153
    data2 = [x * key for x in data]
    nodes2, zero2 = create_linked_list(data2)
    n_total2 = len(nodes2)
    mix(nodes2, 10)
    ans2 = get_grove_coordinates(zero2, n_total2)
    
    sys.stdout.write(f"{ans1}\n{ans2}\n")

if __name__ == "__main__":
    main()