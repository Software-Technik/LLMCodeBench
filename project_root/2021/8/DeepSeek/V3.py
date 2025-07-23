import sys

def part1(data):
    total = 0
    for line in data:
        _, output = line.split('|')
        segments = output.split()
        for s in segments:
            length = len(s)
            if length in {2, 3, 4, 7}:
                total += 1
    return total

def part2(data):
    total = 0
    for line in data:
        input_part, output_part = line.split('|')
        input_segments = input_part.split()
        output_segments = output_part.split()
        
        # Find 1, 4, 7, 8
        one = next(s for s in input_segments if len(s) == 2)
        four = next(s for s in input_segments if len(s) == 4)
        seven = next(s for s in input_segments if len(s) == 3)
        eight = next(s for s in input_segments if len(s) == 7)
        
        # Find 0, 6, 9
        len_six_segments = [s for s in input_segments if len(s) == 6]
        nine = next(s for s in len_six_segments if len(set(s) & set(four)) == 4)
        zero = next(s for s in len_six_segments if len(set(s) & set(one)) == 2 and s != nine)
        six = next(s for s in len_six_segments if s not in {zero, nine})
        
        # Find 2, 3, 5
        len_five_segments = [s for s in input_segments if len(s) == 5]
        three = next(s for s in len_five_segments if len(set(s) & set(one)) == 2)
        five = next(s for s in len_five_segments if len(set(s) & set(four)) == 3 and s != three)
        two = next(s for s in len_five_segments if s not in {three, five})
        
        # Create mapping
        mapping = {
            ''.join(sorted(zero)): '0',
            ''.join(sorted(one)): '1',
            ''.join(sorted(two)): '2',
            ''.join(sorted(three)): '3',
            ''.join(sorted(four)): '4',
            ''.join(sorted(five)): '5',
            ''.join(sorted(six)): '6',
            ''.join(sorted(seven)): '7',
            ''.join(sorted(eight)): '8',
            ''.join(sorted(nine)): '9'
        }
        
        # Decode output
        value = ''.join(mapping[''.join(sorted(s))] for s in output_segments)
        total += int(value)
    return total

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")