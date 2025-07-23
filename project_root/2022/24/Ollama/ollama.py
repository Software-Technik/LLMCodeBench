import sys

def part1(data):
    h, w = len(data), len(data[0])
    blizzards = parse_data(data)
    start = (0, 1)
    target = (h - 1, w - 2)
    areas = {(y, x) for y in range(1, h - 1) for x in range(1, w - 1)}
    areas.add(start)
    areas.add(target)

    queue = {(start, 0)}
    seen = set()

    while queue:
        blizzards = [((bliz_pos[0], (bliz_pos[1] + bliz_dir[1] + w - 3) % (w - 2) + 1) if bliz_dir[0] == 0 else ((bliz_pos[0] + bliz_dir[0] + h - 3) % (h - 2) + 1, bliz_pos[1]), bliz_dir) for bliz_pos, bliz_dir in blizzards]
        avaliable_areas = areas - {i[0] for i in blizzards}

        new_queue = set()
        for pos, history in queue:
            if pos == target:
                return history
            state = (pos, history)
            if state in seen:
                continue
            seen.add(state)

            for d in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if new_pos in avaliable_areas:
                    new_queue.add((new_pos, history + 1))
        queue = new_queue

def part2(data):
    h, w = len(data), len(data[0])
    blizzards = parse_data(data)
    start = (0, 1)
    target = (h - 1, w - 2)
    areas = {(y, x) for y in range(1, h - 1) for x in range(1, w - 1)}
    areas.add(start)
    areas.add(target)

    targets = [target, start, target]
    curr_target = targets.pop(0)
    records = []

    queue = {(start, 0)}
    seen = set()
    goal = False

    while queue:
        if not goal:
            blizzards = [((bliz_pos[0], (bliz_pos[1] + bliz_dir[1] + w - 3) % (w - 2) + 1) if bliz_dir[0] == 0 else ((bliz_pos[0] + bliz_dir[0] + h - 3) % (h - 2) + 1, bliz_pos[1]), bliz_dir) for bliz_pos, bliz_dir in blizzards]
            avaliable_areas = areas - {i[0] for i in blizzards}

        goal = False
        new_queue = set()
        for pos, history in queue:
            if pos == curr_target:
                records.append(history)
                if targets:
                    curr_target = targets.pop(0)
                    new_queue = {(pos, 0)}
                    seen = set()
                    goal = True
                    break
                else:
                    return sum(records)

            state = (pos, history)
            if state in seen:
                continue
            seen.add(state)

            for d in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if new_pos in avaliable_areas:
                    new_queue.add((new_pos, history + 1))
        queue = new_queue

def parse_data(data):
    directions = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }
    blizzards = [((y, i), directions[c]) for y, line in enumerate(data[1:-1], 1) for i, c in enumerate(line[1:-1], 1) if c in "><^v"]
    return blizzards

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")