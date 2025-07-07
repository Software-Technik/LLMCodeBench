import sys
lines = open(sys.argv[1]).read().splitlines()
prop = []
for line in lines:
    parts = line.split(": ")[1].split(", ")
    vals = [int(p.split()[1]) for p in parts]
    prop.append((vals[0], vals[1], vals[2], vals[3], vals[4]))
n = len(prop)
def get_best(max_cal):
    best = 0
    def dfs(i, rem, cap, dur, fla, tex, cal):
        nonlocal best
        if i == n - 1:
            v = rem
            cap += v * prop[i][0]; dur += v * prop[i][1]; fla += v * prop[i][2]; tex += v * prop[i][3]; cal += v * prop[i][4]
            if max_cal == -1 or cal == max_cal:
                a = cap if cap > 0 else 0; b = dur if dur > 0 else 0
                c = fla if fla > 0 else 0; d = tex if tex > 0 else 0
                score = a * b * c * d
                if score > best: best = score
        else:
            ci = prop[i]
            for v in range(rem + 1):
                dfs(i + 1, rem - v, cap + v * ci[0], dur + v * ci[1], fla + v * ci[2], tex + v * ci[3], cal + v * ci[4])
    dfs(0, 100, 0, 0, 0, 0, 0)
    return best
p1 = get_best(-1)
p2 = get_best(500)
sys.stdout.write(f"{p1}\n{p2}\n")