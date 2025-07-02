import sys
import re

def part1(data):
        nums = re.findall(r"-?\d+", data[0])
        return sum(int(i) for i in nums)

def part2(data):
    doc = data[0]
    while doc.count(':"red"') > 0:
        idx = doc.index(':"red"')

        doc_left = doc[:idx]
        left_bracket_pos = doc_left.rindex("{")
        while doc_left[left_bracket_pos + 1 :].count("}") - doc_left[left_bracket_pos + 1 :].count("{") > 0:
            left_bracket_pos = doc_left.rindex("{", 0, left_bracket_pos)

        doc_right = doc[idx:]
        right_bracket_pos = doc_right.index("}")
        while doc_right[:right_bracket_pos].count("{") - doc_right[:right_bracket_pos].count("}") > 0:
            right_bracket_pos = doc_right.index("}", right_bracket_pos + 1)

        doc = doc[:left_bracket_pos] + doc[right_bracket_pos + idx + 1 :]

    return part1([doc])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")