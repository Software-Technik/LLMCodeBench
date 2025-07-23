import sys

def solve(data):
    ingredients = parse_ingredients(data)
    n = len(ingredients)
    best1 = 0
    best2 = 0
    for choice in get_permutations_from_sum(n, 100):
        cap_total, dur_total, fla_total, tex_total, cal_total = 0, 0, 0, 0, 0
        for i in range(n):
            cap, dur, fla, tex, cal = ingredients[i]
            amt = choice[i]
            cap_total += amt * cap
            dur_total += amt * dur
            fla_total += amt * fla
            tex_total += amt * tex
            cal_total += amt * cal
        cap_total = max(0, cap_total)
        dur_total = max(0, dur_total)
        fla_total = max(0, fla_total)
        tex_total = max(0, tex_total)
        score = cap_total * dur_total * fla_total * tex_total
        if score > best1:
            best1 = score
        if cal_total == 500 and score > best2:
            best2 = score
    return best1, best2

def parse_ingredients(data):
    ingredients = []
    for line in data:
        parts = line.split(': ')
        rest = parts[1].split(', ')
        cap = int(rest[0].split()[1])
        dur = int(rest[1].split()[1])
        fla = int(rest[2].split()[1])
        tex = int(rest[3].split()[1])
        cal = int(rest[4].split()[1])
        ingredients.append((cap, dur, fla, tex, cal))
    return ingredients

def get_permutations_from_sum(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in get_permutations_from_sum(length - 1, total_sum - value):
                yield (value,) + permutation

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    p1, p2 = solve(data)
    sys.stdout.write(f"{p1}\n{p2}\n")