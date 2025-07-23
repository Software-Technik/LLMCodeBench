import os
import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

def line_transform(line):
    l, r = line.split("=")
    l = l.strip()
    r = r.strip()
    return (l, r)

lines = [line_transform(line) for line in lines]

mem1 = {}
mem2 = {}
current_mask = None
ones_mask1 = 0
zeroes_mask1 = 0
base_mask2 = 0
float_positions = []
float_clear_mask = 0

for l, r in lines:
    if l.startswith("mask"):
        mask = r
        ones_mask1 = 0
        zeroes_mask1 = 0
        base_mask2 = 0
        float_positions = []
        for i, char in enumerate(mask):
            bit_pos = 35 - i
            if char == '1':
                ones_mask1 |= (1 << bit_pos)
                base_mask2 |= (1 << bit_pos)
            elif char == '0':
                zeroes_mask1 |= (1 << bit_pos)
            elif char == 'X':
                float_positions.append(bit_pos)
        float_clear_mask = 0
        for pos in float_positions:
            float_clear_mask |= (1 << pos)
    else:
        val = int(r)
        addr_val = int(l[4:l.find(']')])
        write_val1 = (val | ones_mask1) & ~zeroes_mask1
        mem1[addr_val] = write_val1

        base_addr = (addr_val | base_mask2) & ~float_clear_mask
        n = len(float_positions)
        for i in range(1 << n):
            float_mask = 0
            for j in range(n):
                if i & (1 << j):
                    float_mask |= (1 << float_positions[j])
            final_addr = base_addr | float_mask
            mem2[final_addr] = val

result1 = sum(mem1.values())
result2 = sum(mem2.values())
print(result1, result2)