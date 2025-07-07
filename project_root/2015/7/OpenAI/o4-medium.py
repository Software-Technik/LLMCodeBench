import sys

def main():
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f]
    ops = {}
    for line in lines:
        src, dest = line.split(" -> ")
        tokens = src.split()
        if len(tokens) == 1:
            ops[dest] = ("ASSIGN", [tokens[0]])
        elif len(tokens) == 2:
            ops[dest] = ("NOT", [tokens[1]])
        else:
            a, op, b = tokens
            ops[dest] = (op, [a, b])
    def make_eval(ops_map):
        memo = {}
        def e(x):
            if x.isdigit():
                return int(x)
            if x in memo:
                return memo[x]
            op, args = ops_map[x]
            if op == "ASSIGN":
                v = e(args[0])
            elif op == "NOT":
                v = ~e(args[0]) & 0xFFFF
            elif op == "AND":
                v = e(args[0]) & e(args[1])
            elif op == "OR":
                v = e(args[0]) | e(args[1])
            elif op == "LSHIFT":
                v = e(args[0]) << int(args[1])
            elif op == "RSHIFT":
                v = e(args[0]) >> int(args[1])
            memo[x] = v & 0xFFFF
            return memo[x]
        return e
    eval1 = make_eval(ops)
    part1 = eval1("a")
    ops2 = ops.copy()
    ops2["b"] = ("ASSIGN", [str(part1)])
    eval2 = make_eval(ops2)
    part2 = eval2("a")
    sys.stdout.write(f"{part1}\n{part2}\n")

if __name__ == "__main__":
    main()