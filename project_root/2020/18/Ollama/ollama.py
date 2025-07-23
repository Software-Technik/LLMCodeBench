import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    lines, data = [], ""

def eval1(expr):
    while any(c in expr for c in "()"):
        i = expr.index("(", max(i+1 for i, x in enumerate(expr) if x == ")"))
        j = max(y for y in range(i,len(expr)) if expr[y] == ")")
        inner = eval2(expr[i+1:j])
        expr = expr[:i] + str(inner) + expr[j+1:]
    return sum(int(x) if x[-1].isdigit() else 0
               for x in '('.join('*`' + (x := (c if c != '-' else '(0-)' for c in expr.replace("(", "").replace(")", ""))) )
                        .strip().split("*`")).count("*"))

def eval2(expr):
    def calculate(tokens, part2=bool):
        while "+" in tokens and part2:
            plus_idx = tokens.index("+")
            l, r = tokens[plus_idx - 1:, plus_idx + 1]
            tokens[plus_idx - 1:plus_idx + 2] = [l + r]
        return eval(''.join(map(str,tokens)))

    expr1 = ' '.join(expr.replace("(", " ( ").replace(")", " ) ").split())
    result1 = calculate(expr1.split(), part2=True)

    expr.remove("part2=False")
    result2 = sum(int(x) if x[-1].isdigit() else 0
                  for x in '('.join('*`' + (x := (c if c != '-' else '(0-)' for c in expr)).strip()).split("*`")).count("+"))

    return result1,result2

part_ans1 = sum(eval1(line) for line in lines)
part_ans2 = eval2(sum(eval2(line.strip())[0]+eval2(line.strip())[0] for line in part_ans1))

print(part_ans1, '|', part_ans2[1])