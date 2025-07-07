import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        lines = f.read().splitlines()
except:
    data, lines = "", []

def tokenize(s):
    s = s.replace("(", " ( ").replace(")", " ) ")
    chunks = s.split()
    tokens = []
    for chunk in chunks:
        if chunk in "()+*-":
            tokens.append(chunk)
        else:
            tokens.append(int(chunk))
    return tokens

def calc(tokens, part2):
    if part2:
        while "+" in tokens:
            plus_idx = tokens.index("+")
            tokens = tokens[:plus_idx - 1] + [tokens[plus_idx - 1] + tokens[plus_idx + 1]] + tokens[plus_idx + 2:]
    running_val = tokens[0]
    i = 1
    while i < len(tokens):
        if tokens[i] == "+":
            running_val += tokens[i + 1]
        elif tokens[i] == "*":
            running_val *= tokens[i + 1]
        i += 2
    return running_val

def eval2(s, part2):
    tokens = tokenize(s)
    return calc(tokens, part2)

def repl_innermost(expr, part):
    while '(' in expr:
        deepest = expr.rfind('(')
        shallowest = expr.find(')', deepest)
        inner_val = str(eval2(expr[deepest+1:shallowest], part))
        expr = expr[:deepest] + inner_val + expr[shallowest+1:]
    return expr

result1 = result2 = 0
for line in lines:
    result1 += eval2(repl_innermost(line, False), False)
    result2 += eval2(repl_innermost(line, True), True)

print(result1, result2)