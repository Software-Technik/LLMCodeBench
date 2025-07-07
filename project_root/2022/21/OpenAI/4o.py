import sys

def part1(data):
    nums = {}
    opes = {}

    for line in data:
        key, ope = line.split(": ")
        if ope.isnumeric():
            nums[key] = int(ope)
        else:
            opes[key] = ope.split(" ")

    while "root" in opes:
        del_keys = []

        for key, (x, o, y) in opes.items():
            if isinstance(x, str) and x in nums:
                x = nums[x]
            if isinstance(y, str) and y in nums:
                y = nums[y]

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
                opes[key] = [x, o, y]

        for key in del_keys:
            del opes[key]

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
            opes[key] = ope.split(" ")

    while True:
        del_keys = []
        replace = False

        for key, (x, o, y) in opes.items():
            if isinstance(x, str) and x in nums:
                x = nums[x]
                replace = True
            if isinstance(y, str) and y in nums:
                y = nums[y]
                replace = True

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
                replace = True
            else:
                opes[key] = (x, o, y)

        for key in del_keys:
            del opes[key]
        
        if not replace:
            break

    x, o, y = opes["root"]
    if isinstance(x, int):
        x, y = y, x

    num = y

    while x != "humn":
        x, o, y = opes[x]
        if isinstance(x, str):
            if o == "+":
                num -= y
            elif o == "-":
                num += y
            elif o == "*":
                num //= y
            elif o == "/":
                num *= y
            x = x
        else:
            if o == "+":
                num -= x
            elif o == "-":
                num = x - num
            elif o == "*":
                num //= x
            elif o == "/":
                num = x // num
            x = y

    return num

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")