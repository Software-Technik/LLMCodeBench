import sys

def part1(data):
    nums = {}
    opes = {}

    for line in data:
        key, ope = line.split(": ")
        if ope.isnumeric():
            nums[key] = int(ope)
        else:
            opes[key] = ope.split()

    while "root" in opes:
        del_keys = []
        for key, (x, o, y) in opes.items():
            if isinstance(x, str):
                if x in nums:
                    x = nums[x]
                elif x.isnumeric():
                    x = int(x)
            if isinstance(y, str):
                if y in nums:
                    y = nums[y]
                elif y.isnumeric():
                    y = int(y)
            if isinstance(x, int) and isinstance(y, int):
                if o == "+":
                    nums[key] = x + y
                elif o == "*":
                    nums[key] = x * y
                elif o == "-":
                    nums[key] = x - y
                elif o == "/":
                    nums[key] = x // y
                del_keys.append(key)
            else:
                opes[key] = (x, o, y)
        for key in del_keys:
            opes.pop(key, None)
    return nums["root"]

def part2(data):
    nums = {}
    opes = {}

    for line in data:
        key, ope = line.split(": ")
        if key == "humn":
            continue
        if ope.isnumeric():
            nums[key] = int(ope)
        else:
            opes[key] = ope.split()

    changed = True
    while changed:
        changed = False
        del_keys = []
        for key, (x, o, y) in opes.items():
            if isinstance(x, str):
                if x in nums:
                    x = nums[x]
                    changed = True
                elif x.isnumeric():
                    x = int(x)
            if isinstance(y, str):
                if y in nums:
                    y = nums[y]
                    changed = True
                elif y.isnumeric():
                    y = int(y)
            if isinstance(x, int) and isinstance(y, int):
                if o == "+":
                    nums[key] = x + y
                elif o == "-":
                    nums[key] = x - y
                elif o == "*":
                    nums[key] = x * y
                elif o == "/":
                    nums[key] = x // y
                del_keys.append(key)
                changed = True
            else:
                opes[key] = (x, o, y)
        for key in del_keys:
            opes.pop(key, None)

    x, _, y = opes["root"]
    if isinstance(x, int):
        x, y = y, x

    num = y
    while x != "humn":
        a, o, b = opes[x]
        if isinstance(a, str):
            if o == "+":
                num -= b
            elif o == "-":
                num += b
            elif o == "*":
                num //= b
            elif o == "/":
                num *= b
            x = a
        else:
            if o == "+":
                num -= a
            elif o == "-":
                num = a - num
            elif o == "*":
                num //= a
            elif o == "/":
                num = a // num
            x = b
    return num

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")