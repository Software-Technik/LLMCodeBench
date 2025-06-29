import sys



# Part one
def part1(data):
    location = 0 + 0j
    current_direction = 1j
    for i in data:
        turn_direction = i[0]
        distance = int(i[1:])
        if turn_direction == 'R':
            current_direction *= -1j
        else:
            current_direction *= 1j
        location += current_direction * distance
    return abs(location.real) + abs(location.imag)



# Part two
def part2(data):
    location = 0 + 0j
    current_direction = 1j
    visited = set()
    for i in data:
        turn_direction = i[0]
        distance = int(i[1:])
        if turn_direction == 'R':
            current_direction *= -1j
        else:
            current_direction *= 1j
        for _ in range(distance):
            location += current_direction
            if location in visited:
                return abs(location.real) + abs(location.imag)
            visited.add(location)
    

inout_strings = sys.argv[1]

with open(inout_strings) as f:
    data = f.read()
    
data = list(map(str.strip, data.split(',')))

sys.stdout.write(f"{part1(data)} {part2(data)}") 
