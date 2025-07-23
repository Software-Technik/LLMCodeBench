import sys
import math

def part1(text: str) -> int:
    lines = text.splitlines()
    times = list(map(int, lines[0].split(":", maxsplit=1)[1].split()))
    distances = list(map(int, lines[1].split(":", maxsplit=1)[1].split()))
    
    total = 1
    for time, distance in zip(times, distances):
        sqrt_val = math.sqrt(time**2 - 4 * distance)
        low = math.ceil((time - sqrt_val) / 2)
        if low * (time - low) <= distance:
            low += 1
        
        high = math.floor((time + sqrt_val) / 2)
        if high * (time - high) <= distance:
            high -= 1
        
        total *= high - low + 1
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    time = int("".join(lines[0].split(":", maxsplit=1)[1].split()))
    distance = int("".join(lines[1].split(":", maxsplit=1)[1].split()))
    
    sqrt_val = math.sqrt(time**2 - 4 * distance)
    low = math.ceil((time - sqrt_val) / 2)
    if low * (time - low) <= distance:
        low += 1
    
    high = math.floor((time + sqrt_val) / 2)
    if high * (time - high) <= distance:
        high -= 1
    
    return high - low + 1 if high >= low else 0

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")