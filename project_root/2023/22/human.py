import sys
from collections import namedtuple
from dataclasses import dataclass
import copy

Cube = namedtuple("Cube", ["x", "y", "z"])

@dataclass
class Brick:
    start: Cube
    end: Cube
    brick_id: int

def cubes(brick_id: int) -> list[Cube]:
    brick = bricks[brick_id]
    if brick.start.x != brick.end.x:
        for x in range(min(brick.start.x, brick.end.x), max(brick.start.x, brick.end.x) + 1):
            yield (x, brick.start.y, brick.start.z)
    elif brick.start.y != brick.end.y:
        for y in range(min(brick.start.y, brick.end.y), max(brick.start.y, brick.end.y) + 1):
            yield (brick.start.x, y, brick.start.z)
    else:
        for z in range(min(brick.start.z, brick.end.z), max(brick.start.z, brick.end.z) + 1):
            yield (brick.start.x, brick.start.y, z)

def is_falling(brick: Brick, invisible_brick_id: int = -1) -> bool:
    if brick.brick_id == invisible_brick_id:
        return False
    is_vertical = brick.start.z != brick.end.z
    if is_vertical:
        z = min(brick.start.z, brick.end.z)
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

def drop_tick(invisible_brick_id: int = -1) -> set[int]:
    falling_ids = set()
    max_z = max(z for _, _, z in world.keys())
    min_z = 1 if invisible_brick_id == -1 else max(bricks[invisible_brick_id].start.z, bricks[invisible_brick_id].end.z) + 1

    for z in range(min_z, max_z + 1):
        current = (b for b in bricks if b.start.z == z or b.end.z == z)
        for brick in current:
            if not is_falling(brick, invisible_brick_id):
                continue
            falling_ids.add(brick.brick_id)
            for x, y, z in cubes(brick.brick_id):
                del world[(x, y, z)]
                world[(x, y, z - 1)] = brick.brick_id
            if invisible_brick_id != -1:
                continue
            brick.start = Cube(brick.start.x, brick.start.y, brick.start.z - 1)
            brick.end = Cube(brick.end.x, brick.end.y, brick.end.z - 1)
    return falling_ids

def drop_until_done():
    while len(drop_tick()) > 0:
        pass

def part1(text):
    global bricks, world
    bricks, world = [], {}
    for line in text.strip().splitlines():
        a, b = line.strip().split("~")
        start = Cube(*map(int, a.split(",")))
        end = Cube(*map(int, b.split(",")))
        brick = Brick(start, end, len(bricks))
        bricks.append(brick)
        for x, y, z in cubes(brick.brick_id):
            world[(x, y, z)] = brick.brick_id

    drop_until_done()

    count = 0
    for brick in bricks:
        backup = world.copy()
        if len(drop_tick(invisible_brick_id=brick.brick_id)) == 0:
            count += 1
        world = backup
    return count

def part2(text):
    global bricks, world
    bricks, world = [], {}
    for line in text.strip().splitlines():
        a, b = line.strip().split("~")
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
        bricks_copy = copy.deepcopy(bricks)
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