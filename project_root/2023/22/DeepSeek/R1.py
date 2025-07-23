import sys
from collections import deque, defaultdict

Cube = namedtuple("Cube", ["x", "y", "z"])

@dataclass
class Brick:
    start: Cube
    end: Cube
    brick_id: int

def cubes(brick):
    if brick.start.x != brick.end.x:
        for x in range(min(brick.start.x, brick.end.x), max(brick.start.x, brick.end.x) + 1):
            yield (x, brick.start.y, brick.start.z)
    elif brick.start.y != brick.end.y:
        for y in range(min(brick.start.y, brick.end.y), max(brick.start.y, brick.end.y) + 1):
            yield (brick.start.x, y, brick.start.z)
    else:
        for z in range(min(brick.start.z, brick.end.z), max(brick.start.z, brick.end.z) + 1):
            yield (brick.start.x, brick.start.y, z)

def drop_bricks(bricks):
    bricks = sorted(bricks, key=lambda b: min(b.start.z, b.end.z))
    height_map = defaultdict(int)
    world = {}
    for brick in bricks:
        x_min = min(brick.start.x, brick.end.x)
        x_max = max(brick.start.x, brick.end.x)
        y_min = min(brick.start.y, brick.end.y)
        y_max = max(brick.start.y, brick.end.y)
        min_z = min(brick.start.z, brick.end.z)
        max_below = 0
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                if (x, y) in height_map:
                    if height_map[(x, y)] > max_below:
                        max_below = height_map[(x, y)]
        drop = min_z - (max_below + 1)
        new_start = Cube(brick.start.x, brick.start.y, brick.start.z - drop)
        new_end = Cube(brick.end.x, brick.end.y, brick.end.z - drop)
        brick.start = new_start
        brick.end = new_end
        for (x, y, z) in cubes(brick):
            world[(x, y, z)] = brick.brick_id
            if z > height_map[(x, y)]:
                height_map[(x, y)] = z
    return bricks, world

def build_graph(bricks, world):
    supports = defaultdict(set)
    supported_by = defaultdict(set)
    for brick in bricks:
        brick_id = brick.brick_id
        min_z = min(brick.start.z, brick.end.z)
        if min_z == 1:
            continue
        x_min = min(brick.start.x, brick.end.x)
        x_max = max(brick.start.x, brick.end.x)
        y_min = min(brick.start.y, brick.end.y)
        y_max = max(brick.start.y, brick.end.y)
        below_bricks = set()
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                pos = (x, y, min_z - 1)
                if pos in world:
                    below_id = world[pos]
                    if below_id != brick_id:
                        below_bricks.add(below_id)
        for below_id in below_bricks:
            supports[below_id].add(brick_id)
            supported_by[brick_id].add(below_id)
    return supports, supported_by

def part1(bricks, supports, supported_by):
    count = 0
    for brick in bricks:
        brick_id = brick.brick_id
        safe = True
        for supported_id in supports.get(brick_id, set()):
            if len(supported_by.get(supported_id, set())) == 1:
                safe = False
                break
        if safe:
            count += 1
    return count

def part2(bricks, supports, supported_by):
    total = 0
    for brick in bricks:
        start_id = brick.brick_id
        falling = set([start_id])
        queue = deque([start_id])
        while queue:
            cur = queue.popleft()
            for nxt in supports.get(cur, set()):
                if nxt in falling:
                    continue
                if supported_by[nxt].issubset(falling):
                    falling.add(nxt)
                    queue.append(nxt)
        total += len(falling) - 1
    return total

def parse(text):
    bricks = []
    for i, line in enumerate(text.strip().splitlines()):
        a, b = line.strip().split("~")
        start = Cube(*map(int, a.split(",")))
        end = Cube(*map(int, b.split(",")))
        bricks.append(Brick(start, end, i))
    return bricks

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
    bricks = parse(text)
    bricks, world = drop_bricks(bricks)
    supports, supported_by = build_graph(bricks, world)
    ans1 = part1(bricks, supports, supported_by)
    ans2 = part2(bricks, supports, supported_by)
    sys.stdout.write(f"{ans1} {ans2}\n")