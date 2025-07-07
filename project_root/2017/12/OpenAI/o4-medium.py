import sys

def main():
    graph = {}
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if line:
                a, bs = line.split(" <-> ")
                graph[int(a)] = [int(x) for x in bs.split(", ")]
    visited = {0}
    stack = [0]
    while stack:
        cur = stack.pop()
        for nbr in graph[cur]:
            if nbr not in visited:
                visited.add(nbr)
                stack.append(nbr)
    part1 = len(visited)
    groups = 1
    for node in graph:
        if node not in visited:
            visited.add(node)
            stack = [node]
            while stack:
                cur = stack.pop()
                for nbr in graph[cur]:
                    if nbr not in visited:
                        visited.add(nbr)
                        stack.append(nbr)
            groups += 1
    print(part1)
    print(groups)

if __name__ == "__main__":
    main()