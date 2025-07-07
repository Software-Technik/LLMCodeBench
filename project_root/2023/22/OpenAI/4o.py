import sys
from collections import namedtuple

Cube = namedtuple("Cube", ["x", "y", "z"])

class Brick:
    def __init__(self, start, end, brick_id):
        self.start = start
        self.end = end
        self.brick_id = brick_id

def cubes(brick_id: int):
    brick = bricks[brick_id]
    if brick.start.x != brick.end.x:
        for x in range(brick.start.x, brick.end.x + 1):
            yield (x, brick.start.y, brick.start.z)
    elif brick.start.y != brick.end.y:
        for y in range(brick.start.y, brick.end.y + 1):
            yield (brick.start.x, y, brick.start.z)
    else:
        for z in range(brick.start.z, brick.end.z + 1):
            yield (brick.start.x, brick.start.y, z)

def is_falling(brick, invisible_brick_id=-1):
    if brick.brick_id == invisible_brick_id:
        return False
    if brick.start.z != brick.end.z:
        z = brick.start.z
        if z == 1:
            return False
        below = world.get((brick.start.x, brick.start.y, z - 1))
        return below in [None, invisible_brick_id]
    else:
        if brick.start.z == 1:
            return False
        for x, y, z in cubes(brick.brick_id):
            below = world.get((x, y, z - 1))
            if below not in [None, invisible_brick_id]:
                return False
        return True

def drop_tick(invisible_brick_id=-1):
    falling_ids = set()
    bricks_to_process = sorted((b for b in bricks if b.start.z > 0), key=lambda b: b.start.z, reverse=True)
    for brick in bricks_to_process:
        if is_falling(brick, invisible_brick_id):
            falling_ids.add(brick.brick_id)
            for x, y, z in cubes(brick.brick_id):
                del world[(x, y, z)]
                world[(x, y, z - 1)] = brick.brick_id
            brick.start = Cube(brick.start.x, brick.start.y, brick.start.z - 1)
            brick.end = Cube(brick.end.x, brick.end.y, brick.end.z - 1)
    return falling_ids

def drop_until_done():
    while drop_tick():
        pass

def part1(text):
    global bricks, world
    bricks, world = [], {}
    for line in text.strip().splitlines():
        a, b = line.split("~")
        start = Cube(*map(int, a.split(",")))
        end = Cube(*map(int, b.split(",")))
        brick = Brick(start, end, len(bricks))
        bricks.append(brick)
        for x, y, z in cubes(brick.brick_id):
            world[(x, y, z)] = brick.brick_id

    drop_until_done()

    count = 0
    for brick in bricks:
        if not drop_tick(invisible_brick_id=brick.brick_id):
            count += 1
    return count

def part2(text):
    global bricks, world
    bricks, world = [], {}
    for line in text.strip().splitlines():
        a, b = line.split("~")
        start = Cube(*map(int, a.split(",")))
        end = Cube(*map(int, b.split(",")))
        brick = Brick(start, end, len(bricks))
        bricks.append(brick)
        for x, y, z in cubes(brick.brick_id):
            world[(x, y, z)] = brick.brick_id

    drop_until_done()

    total = 0
    for brick in bricks:
        world_copy = world.copy()
        bricks_copy = [Brick(b.start, b.end, b.brick_id) for b in bricks]
        falling_ids = set()
        while True:
            before = len(falling_ids)
            falling_ids.update(drop_tick(invisible_brick_id=brick.brick_id))
            if len(falling_ids) == before:
                break
        total += len(falling_ids)
        world = world_copy
        bricks = bricks_copy
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")