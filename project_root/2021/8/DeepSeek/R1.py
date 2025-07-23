import sys

def preprocess(data):
    processed = []
    for line in data:
        parts = line.split('|')
        input_part = parts[0].split()
        output_part = parts[1].split()
        processed.append((input_part, output_part))
    return processed

def part1(processed_data):
    total = 0
    for d in processed_data:
        output_tokens = d[1]
        for token in output_tokens:
            l = len(token)
            if l in [2, 3, 4, 7]:
                total += 1
    return total

def part2(processed_data):
    total = 0
    for d in processed_data:
        input_tokens, output_tokens = d
        patterns = [''.join(sorted(p)) for p in input_tokens]
        mapping = {}
        len5s = []
        len6s = []
        one_str = None
        four_str = None
        for p in patterns:
            l = len(p)
            if l == 2:
                mapping[p] = '1'
                one_str = p
            elif l == 3:
                mapping[p] = '7'
            elif l == 4:
                mapping[p] = '4'
                four_str = p
            elif l == 7:
                mapping[p] = '8'
            elif l == 5:
                len5s.append(p)
            elif l == 6:
                len6s.append(p)
        one_set = set(one_str) if one_str is not None else set()
        four_set = set(four_str) if four_str is not None else set()
        for p in len6s:
            if len(set(p) & four_set) == 4:
                mapping[p] = '9'
            elif len(set(p) & one_set) == 2:
                mapping[p] = '0'
            else:
                mapping[p] = '6'
        for p in len5s:
            if len(set(p) & one_set) == 2:
                mapping[p] = '3'
            elif len(set(p) & four_set) == 2:
                mapping[p] = '2'
            else:
                mapping[p] = '5'
        value_str = ''.join(mapping[''.join(sorted(token))] for token in output_tokens)
        total += int(value_str)
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

processed_data = preprocess(data)
sys.stdout.write(f"{part1(processed_data)} {part2(processed_data)}")