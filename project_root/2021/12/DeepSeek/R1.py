import sys
from functools import lru_cache

def main():
    with open(sys.argv[1]) as f:
        data = [line.strip().split("-") for line in f if line.strip()]

    graph = {}
    for a, b in data:
        if a != "end" and b != "start":
            if a not in graph:
                graph[a] = set()
            graph[a].add(b)
        if b != "end" and a != "start":
            if b not in graph:
                graph[b] = set()
            graph[b].add(a)
    
    @lru_cache(maxsize=None)
    def dfs(current, visited, repeat_available):
        if current == "end":
            return 1
        total = 0
        for neighbor in graph.get(current, set()):
            if neighbor.isupper():
                total += dfs(neighbor, visited, repeat_available)
            else:
                if neighbor not in visited:
                    total += dfs(neighbor, visited | {neighbor}, repeat_available)
                elif repeat_available:
                    total += dfs(neighbor, visited, False)
        return total

    part1 = dfs('start', frozenset(['start']), False)
    part2 = dfs('start', frozenset(['start']), True)
    sys.stdout.write(f"{part1} {part2}")

if __name__ == "__main__":
    main()