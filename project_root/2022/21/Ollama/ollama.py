import sys

def part1(data):
    nums, opes = {}, {}

    for line in data:
        key, ope = line.split(": ")
        if ope.isnumeric():
            nums[key] = int(ope)
        else:
            opes[key] = ope.split(" ")

    while "root" in opes:
        for key, (x, o, y) in list(opes.items()):
            x = nums.get(x, int(x)) if str.isnumeric(str(x)) else x
            y = nums.get(y, int(y)) if str.isnumeric(str(y)) else y

            if isinstance(x, int) and isinstance(y, int):
                match o:
                    case "+": val = x + y
                    case "-": val = x - y
                    case "*": val = x * y
                    case "/": val = x // y
                nums[key] = val
                del opes[key]

    return nums["root"]

def part2(data):
    nums, opes = {}, {}

    for line in data:
        key, ope = line.split(": ")
        if ope.isnumeric():
            nums[key] = int(ope)
        elif key != "humn":
            opes[key] = ope.split(" ")

    while "root" not in nums:
        for key, (x, o, y) in list(opes.items()):
            x = nums.get(x, int(x)) if str.isnumeric(str(x)) else x
            y = nums.get(y, int(y)) if str.isnumeric(str(y)) else y

            if isinstance(x, int) and isinstance(y, int):
                match o:
                    case "+": val = x + y
                    case "-": val = x - y
                    case "*": val = x * y
                    case "/": val = x // y
                nums[key] = val
                del opes[key]

    x, o, y = opes["root"]
    if isinstance(x, int):
        solve_for = y
    else:
        solve_for = x

    result = solve_for
    current_key = solve_for

    while current_key != "humn":
        key = None
        for k in opes.keys():
            if solve_for in opes[k]:
                key = k
                break

        current_ope = opes[key]
        if current_ope[0] == solve_for:
            other_val = int(current_ope[2]) if isinstance(int(current_ope[2]), int) else nums[current_ope[2]]
            match current_ope[1]:
                case "+":
                    result -= other_val
                    current_key = None
                case "-":
                    result += other_val
                    current_key = None
                case "*":
                    result //= other_val
                    current_key = None
                case "/":
                    result *= other_val
                    current_key = None
        else:
            other_val = int(current_ope[0]) if isinstance(int(current_ope[1]), int) else nums[current_ope[0]]
            match current_ope[1]:
                case "+":
                    result -= other_val
                    current_key = None
                case "-":
                    result = other_val - result
                    current_key = None
                case "*":
                    result //= other_val
                    current_key = None
                case "/":
                    result = other_val // result
                    current_key = None

        solve_for = key

    return int(result)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")