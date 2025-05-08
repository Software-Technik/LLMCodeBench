import sys


def part1(line):

    def make_filesystem(diskmap):
        blocks = []

        is_file = True
        id = 0
        for x in diskmap:
            x = int(x)
            if is_file:
                blocks += [id] * x
                id += 1
                is_file = False
            else:
                blocks += [None] * x
                is_file = True

        return blocks

    filesystem = make_filesystem(line)

    def move(arr):
        first_free = 0
        while arr[first_free] != None:
            first_free += 1

        i = len(arr) - 1
        while arr[i] == None:
            i -= 1

        while i > first_free:
            arr[first_free] = arr[i]
            arr[i] = None
            while arr[i] == None:
                i -= 1
            while arr[first_free] != None:
                first_free += 1

        return arr

    def checksum(arr):
        ans = 0
        for i, x in enumerate(arr):
            if x != None:
                ans += i * x
        return ans

    ans = checksum(move(filesystem))
    return ans


def part2(line):

    # Allocate a lot of space
    size = [0] * len(line)
    loc = [0] * len(line)

    def make_filesystem(diskmap):
        global loc, size

        blocks = []

        is_file = True
        id = 0
        for x in diskmap:
            x = int(x)
            if is_file:
                loc[id] = len(blocks)
                size[id] = x
                blocks += [id] * x
                id += 1
                is_file = False
            else:
                blocks += [None] * x
                is_file = True

        return blocks

    filesystem = make_filesystem(line)

    def move(arr):
        # Current file to move
        big = 0
        while size[big] > 0:
            big += 1
        big -= 1

        for to_move in range(big, -1, -1):
            # Find first free space that works
            free_space = 0
            first_free = 0
            while first_free < loc[to_move] and free_space < size[to_move]:
                first_free = first_free + free_space
                free_space = 0
                while arr[first_free] != None:
                    first_free += 1
                while (
                    first_free + free_space < len(arr)
                    and arr[first_free + free_space] == None
                ):
                    free_space += 1

            if first_free >= loc[to_move]:
                continue

            # Move file by swapping block values
            for idx in range(first_free, first_free + size[to_move]):
                arr[idx] = to_move
            for idx in range(loc[to_move], loc[to_move] + size[to_move]):
                arr[idx] = None

        return arr

    def checksum(arr):
        ans = 0
        for i, x in enumerate(arr):
            if x != None:
                ans += i * x
        return ans

    moved = move(filesystem)

    return checksum(moved)


input_path = sys.argv[1]
with open(input_path) as fin:
    line = fin.read().strip()
    print(part1(line), part2(line))
