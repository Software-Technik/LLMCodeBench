import sys
from collections import deque
from itertools import permutations

def main():
    with open(sys.argv[1], 'r') as infile:
        maze = infile.read().splitlines()

    def bfs(start, goal):
        DELTAS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        que = deque([(start, 0)])
        seen = set([start])

        while que:
            (x, y), steps = que.popleft()
            if (x, y) == goal:
                return steps
            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in seen and maze[ny][nx] != '#':
                    seen.add((nx, ny))
                    que.append(((nx, ny), steps + 1))

    coordinates = {}
    for y, row in enumerate(maze):
        for x, value in enumerate(row):
            if value.isdigit():
                coordinates[int(value)] = (x, y)

    num_points = len(coordinates)
    distances = [[0] * num_points for _ in range(num_points)]

    points = sorted(coordinates.keys())
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = bfs(coordinates[points[i]], coordinates[points[j]])
            distances[i][j] = distances[j][i] = dist

    def find_shortest(second_part=False):
        min_dist = float('inf')
        points_to_permute = list(range(1, num_points))
        for path in permutations(points_to_permute):
            current_dist = distances[0][path[0]]
            for a, b in zip(path, path[1:]):
                current_dist += distances[a][b]
            if second_part:
                current_dist += distances[path[-1]][0]
            if current_dist < min_dist:
                min_dist = current_dist
        return min_dist

    print(f"{find_shortest()} {find_shortest(True)}")

if __name__ == "__main__":
    main()