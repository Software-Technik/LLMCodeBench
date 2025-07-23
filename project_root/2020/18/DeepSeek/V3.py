import sys

def tokenize_improved(s):
    s = s.replace("(", " ( ").replace(")", " ) ")
    chunks = s.split()
    relevant_chunks = []
    for chunk in chunks:
        if chunk in "()+*-":
            relevant_chunks.append(chunk)
        else:
            relevant_chunks.append(int(chunk))
    return relevant_chunks

def calc(tokens, part2):
    if part2:
        i = 0
        while i < len(tokens):
            if tokens[i] == '+':
                tokens[i-1] += tokens[i+1]
                del tokens[i:i+2]
                i -= 1
            i += 1
    val = tokens[0]
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = tokens[i+1]
        if op == '+':
            val += num
        elif op == '*':
            val *= num
    return val

def eval_expr(expr, part2):
    tokens = tokenize_improved(expr)
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            sub_expr = []
            while stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()  # Remove '('
            sub_expr.reverse()
            val = calc(sub_expr, part2)
            stack.append(val)
        else:
            stack.append(token)
    return calc(stack, part2)

def main():
    input_path = sys.argv[1]
    with open(input_path) as f:
        lines = f.read().splitlines()

    result1 = sum(eval_expr(line, False) for line in lines)
    result2 = sum(eval_expr(line, True) for line in lines)
    print(result1, result2)

if __name__ == "__main__":
    main()