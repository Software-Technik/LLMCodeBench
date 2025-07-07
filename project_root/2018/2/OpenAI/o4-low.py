import sys

def get_checksum(lines):
    two = three = 0
    for line in lines:
        counts = {}
        for c in line:
            counts[c] = counts.get(c, 0) + 1
        vals = counts.values()
        two += 2 in vals
        three += 3 in vals
    return two * three

def get_common_letters(lines):
    length = len(lines[0])
    for i in range(length):
        seen = {}
        for line in lines:
            key = line[:i] + line[i+1:]
            if key in seen:
                return key
            seen[key] = True

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f if l.strip()]
    checksum = get_checksum(lines)
    common = get_common_letters(lines)
    sys.stdout.write(f"{checksum} {common}")