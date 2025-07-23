import sys
import collections

def propagate_known(nums, opes, skip_set=None):
    if skip_set is None:
        skip_set = set()
    for key in list(opes.keys()):
        left, op_char, right = opes[key]
        if type(left) is str and left.isnumeric():
            left = int(left)
        if type(right) is str and right.isnumeric():
            right = int(right)
        opes[key] = [left, op_char, right]
    
    dependents = collections.defaultdict(list)
    for key, (left, op_char, right) in opes.items():
        if type(left) is str:
            dependents[left].append((key, 0))
        if type(right) is str:
            dependents[right].append((key, 2))
    
    queue = collections.deque()
    for key in nums:
        if key not in skip_set:
            queue.append(key)
    
    while queue:
        k = queue.popleft()
        if k not in dependents:
            continue
        for (op_key, idx) in dependents[k]:
            if op_key not in opes:
                continue
            op_list = opes[op_key]
            if idx == 0:
                if type(op_list[0]) is str and op_list[0] == k:
                    op_list[0] = nums[k]
            elif idx == 2:
                if type(op_list[2]) is str and op_list[2] == k:
                    op_list[2] = nums[k]
            left, op_char, right = op_list
            if isinstance(left, int) and isinstance(right, int):
                if op_char == '+':
                    res = left + right
                elif op_char == '-':
                    res = left - right
                elif op_char == '*':
                    res = left * right
                elif op_char == '/':
                    res = left // right
                nums[op_key] = res
                del opes[op_key]
                if op_key not in skip_set:
                    queue.append(op_key)
    return nums, opes

def part1(data):
    nums = {}
    opes = {}
    for line in data:
        key, ope = line.split(": ")
        if ope.isnumeric():
            nums[key] = int(ope)
        else:
            opes[key] = ope.split()
    nums, opes = propagate_known(nums, opes, set())
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
    skip_set = {'humn'}
    nums, opes = propagate_known(nums, opes, skip_set)
    x, _, y = opes["root"]
    if isinstance(x, int):
        x, y = y, x
    start = x
    num = y
    while start != "humn":
        left, op, right = opes[start]
        if isinstance(left, str):
            if op == '+':
                num -= right
            elif op == '-':
                num += right
            elif op == '*':
                num //= right
            elif op == '/':
                num *= right
            start = left
        else:
            if op == '+':
                num -= left
            elif op == '-':
                num = left - num
            elif op == '*':
                num //= left
            elif op == '/':
                num = left // num
            start = right
    return num

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")