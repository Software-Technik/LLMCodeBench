import sys
import re

def contains_abba(s):
    n = len(s)
    for i in range(n - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

def part1(segments_list):
    count = 0
    for supernet_segments, hypernet_segments in segments_list:
        has_super_abba = any(contains_abba(seg) for seg in supernet_segments)
        has_hyper_abba = any(contains_abba(seg) for seg in hypernet_segments)
        if has_super_abba and not has_hyper_abba:
            count += 1
    return count

def part2(segments_list):
    count = 0
    for supernet_segments, hypernet_segments in segments_list:
        found = False
        for seg in supernet_segments:
            n = len(seg)
            for i in range(n - 2):
                if seg[i] == seg[i+2] and seg[i] != seg[i+1]:
                    bab = seg[i+1] + seg[i] + seg[i+1]
                    for hseg in hypernet_segments:
                        if bab in hseg:
                            found = True
                            break
                    if found:
                        break
            if found:
                break
        count += 1 if found else 0
    return count

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readlines()

segments_list = []
for line in data:
    tokens = re.split(r'\[|\]', line.strip())
    supernet_segments = tokens[0::2]
    hypernet_segments = tokens[1::2]
    segments_list.append((supernet_segments, hypernet_segments))

sys.stdout.write(f"{part1(segments_list)} {part2(segments_list)}")