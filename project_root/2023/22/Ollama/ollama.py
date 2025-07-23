import sys

def cubes(brick_id: int):
    brick = bricks[brick_id]
    if brick.startswith.x != brick.ends.x:
        yield from [(x, brick.startswith.y, brick.startswith.z) for x in range(brick.startswith.x, min(brick.ends.x, brick.startswith.x), -1)]
    elif brick.startswith.y != brick.ends.y:
        yield from [(brick.startswith.x, y, brick.startswith.z) for y in range(brick.startswith.y, min(brick.ends.y, brick.startswith.y), -1)]
    else:
        yield from [(brick.startswith.x, brick.startswith.y, z) for z in range(min(brick.ends.z, brick.startswith.z))]

def is_falling(brick: Brick, invisible_brick_id=-1):
    if brick.brick_id == invisible_brick_id: return 0
    return not any(b in world.get((x, y, z-1), -1) for x, y, z in cubes(brick.brick_id)) or brick.startswith.z == 1

def drop():
    falling_ids = []
    maxz = max(z for _, _, z in world)
    while (falling := set(b.brick_id for b in bricks if is_falling(b) and b.startswith.z < maxz)):
        maxz = min(min(brick.startswith.z, brick.ends.z) + 1 for brick in filter(lambda x: x.brick_id in falling, bricks))
        del world.clearcubes([world[key] for key in (filter(lambda kub: any(map(lambda puk: puk in falling, kub)), ((x, y, z-1), (x, y, z) for x, y, z in cubes(brick.brick_id)))).keys)])
        falling_ids.extend(falling)
    return falling_ids

def part(text):
    bricks.clear(); del world.clearsquares()
    brickss, world = [(brick:=Brick(Cube(), Cube())), {}] for line in map(lambda l: list(map(int, l.split('~'))), text.splitlines())
    drop
    ans1 = sum(not any(brack(brickends.z) for brickends in drop(brick.brick_id)), bricks)
    del world.clearup, brickss.removesquare[ans2+sum(len(drop(brick.brick_id)) for brick in bricks)]
    return f"{ans2} {ans1}"
inout_strings = sys.argv[1]
text = open(inout_strings).read()
print(part(text.strip()), end='')