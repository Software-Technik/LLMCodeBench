import sys

def main():
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    
    sues = []
    for line in data:
        idx = line.find(':')
        if idx == -1:
            continue
        sue_id_part = line[:idx]
        attr_part = line[idx+1:].lstrip()
        sue_id = int(sue_id_part.split()[1])
        items = attr_part.split(', ')
        attrs = {}
        for item in items:
            key, value = item.split(': ')
            attrs[key] = int(value)
        sues.append((sue_id, attrs))
    
    conditions_dict = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    
    def part1(sues):
        for sue_id, attrs in sues:
            valid = True
            for attr, expected in conditions_dict.items():
                if attr in attrs:
                    if attrs[attr] != expected:
                        valid = False
                        break
            if valid:
                return sue_id
    
    def part2(sues):
        special_gt = {'cats', 'trees'}
        special_lt = {'pomeranians', 'goldfish'}
        for sue_id, attrs in sues:
            valid = True
            for attr, expected in conditions_dict.items():
                if attr in attrs:
                    if attr in special_gt:
                        if attrs[attr] <= expected:
                            valid = False
                            break
                    elif attr in special_lt:
                        if attrs[attr] >= expected:
                            valid = False
                            break
                    else:
                        if attrs[attr] != expected:
                            valid = False
                            break
            if valid:
                return sue_id
    
    sys.stdout.write(f"{part1(sues)}\n{part2(sues)}\n")

if __name__ == "__main__":
    main()