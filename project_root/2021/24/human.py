import sys
import z3

def parse_parameters(lines):
    V = []
    for i in range(0, len(lines), 18):  # Jeder Block hat 18 Zeilen
        block = lines[i:i + 18]
        div_z = int(block[4].split()[-1])
        add_x = int(block[5].split()[-1])
        add_y = int(block[15].split()[-1])
        V.append((div_z, add_x, add_y))
    return V


def Solver(V):
    solver = z3.Optimize()
    var = [z3.Int(f"s_{i}") for i in range(14)]
    for i in range(14):
        solver.add(var[i] >= 1, var[i] <= 9)

    z = z3.IntVal(0)
    for i in range(14):
        x = z % 26
        z /= V[i][0]
        z = z3.If(x + V[i][1] != var[i], z * 26 + var[i] + V[i][2], z)
    solver.add(z == 0)
    return solver, var


def part1(data):
    # Part 1
    parsedParams = parse_parameters(data)
    solver, var = Solver(parsedParams)
    solver.maximize(sum([v * 10 ** (13 - i) for i, v in enumerate(var)]))
    solver.check()
    m = solver.model()
    return int("".join(str(m[x]) for x in var))


def part2(data):
    # Part 2
    parsedParams = parse_parameters(data)
    solver, var = Solver(parsedParams)
    solver.minimize(sum([v * 10 ** (13 - i) for i, v in enumerate(var)]))
    solver.check()
    m = solver.model()
    return int("".join(str(m[x]) for x in var))


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")