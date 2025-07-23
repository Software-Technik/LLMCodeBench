import sys
from collections import deque
from math import lcm

def part1(initial_monkeys):
    monkeys = []
    for m in initial_monkeys:
        monkeys.append({
            "items": deque(m["items"]),
            "ope": m["ope"],
            "test": m["test"],
            "target": m["target"],
            "times": 0
        })
    
    for _ in range(20):
        for m in monkeys:
            while m["items"]:
                m["times"] += 1
                worry = m["items"].popleft()
                worry = m["ope"](worry)
                worry //= 3
                test = worry % m["test"] == 0
                target = m["target"][test]
                monkeys[target]["items"].append(worry)
                
    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def part2(initial_monkeys):
    monkeys = []
    for m in initial_monkeys:
        monkeys.append({
            "items": deque(m["items"]),
            "ope": m["ope"],
            "test": m["test"],
            "target": m["target"],
            "times": 0
        })
    
    test_lcm = lcm(*[m["test"] for m in initial_monkeys])
    
    for _ in range(10000):
        for m in monkeys:
            while m["items"]:
                m["times"] += 1
                worry = m["items"].popleft()
                worry = m["ope"](worry)
                worry %= test_lcm
                test = worry % m["test"] == 0
                target = m["target"][test]
                monkeys[target]["items"].append(worry)
                
    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def parse_data(data):
    data = [i.split("\n") for i in ("\n".join(data)).split("\n\n")]
    
    monkeys = []
    for i in data:
        items = list(map(int, i[1].split(":")[1].strip().split(", ")))
        match i[2].split("=")[1].strip().split():
            case ["old", "+", "old"]:
                ope = lambda x: x + x
            case ["old", "+", val]:
                ope = lambda x, val=int(val): x + val
            case ["old", "*", "old"]:
                ope = lambda x: x * x
            case ["old", "*", val]:
                ope = lambda x, val=int(val): x * val
        test = int(i[3].split("by")[1].strip())
        target = [int(i[5].split("monkey")[1].strip()), int(i[4].split("monkey")[1].strip())]
        
        monkey = {"items": items, "ope": ope, "test": test, "target": target}
        monkeys.append(monkey)
        
    return monkeys

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

initial_monkeys = parse_data(data)
sys.stdout.write(f"{part1(initial_monkeys)}\n{part2(initial_monkeys)}\n")