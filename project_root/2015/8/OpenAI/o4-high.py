import sys, ast
code_len=mem_len=new_code_len=0
with open(sys.argv[1]) as f:
    for line in f:
        s=line.strip()
        code_len+=len(s)
        mem_len+=len(ast.literal_eval(s))
        new_code_len+=len(s)+s.count('\\')+s.count('"')+2
print(code_len-mem_len)
print(new_code_len-code_len)