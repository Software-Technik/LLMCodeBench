import sys
from itertools import permutations

def parse_guest_matrix(data):
    guest_dict = {}
    guest_names = set()
    for line in data:
        parts = line.split()
        name1 = parts[0]
        name2 = parts[-1][:-1]
        happy_val = int(parts[3])
        if parts[2] == "lose":
            happy_val = -happy_val
        if name1 not in guest_dict:
            guest_dict[name1] = {}
        guest_dict[name1][name2] = happy_val
        guest_names.add(name1)
        guest_names.add(name2)
    guests = sorted(guest_names)
    n = len(guests)
    name_to_idx = {name: idx for idx, name in enumerate(guests)}
    mat = [[0] * n for _ in range(n)]
    for name1, neighbors in guest_dict.items():
        i = name_to_idx[name1]
        for name2, happy_val in neighbors.items():
            j = name_to_idx[name2]
            mat[i][j] = happy_val
    return guests, mat

def calc_max_happiness_matrix(guests, mat):
    n = len(guests)
    if n == 0:
        return 0
    indices = list(range(1, n))
    best = -10**9
    for p in permutations(indices):
        arr = [0] + list(p)
        total = 0
        for i in range(n):
            left = arr[i-1]
            right = arr[(i+1) % n]
            person = arr[i]
            total += mat[person][left] + mat[person][right]
        if total > best:
            best = total
    return best

def part1(data):
    guests, mat = parse_guest_matrix(data)
    return calc_max_happiness_matrix(guests, mat)

def part2(data):
    guests, mat = parse_guest_matrix(data)
    n_orig = len(guests)
    guests.append("me")
    for row in mat:
        row.append(0)
    mat.append([0] * (n_orig + 1))
    return calc_max_happiness_matrix(guests, mat)

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")