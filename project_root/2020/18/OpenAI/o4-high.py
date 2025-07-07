import sys
lines = open(sys.argv[1]).read().splitlines()
def eval1(s,i=0):
    val=0; op='+'
    while i<len(s):
        c=s[i]
        if c==' ':
            i+=1
        elif c=='(':
            num,i=eval1(s,i+1)
            val=val+num if op=='+' else val*num
        elif c==')':
            return val,i+1
        elif '0'<=c<='9':
            num=0
            while i<len(s) and '0'<=s[i]<='9':
                num=num*10+ord(s[i])-48; i+=1
            val=val+num if op=='+' else val*num
        else:
            op=c; i+=1
    return val,i
def eval2_factor(s,i):
    while i<len(s) and s[i]==' ': i+=1
    if s[i]=='(':
        val,i=eval2_expr(s,i+1)
        return val,i+1
    num=0
    while i<len(s) and '0'<=s[i]<='9':
        num=num*10+ord(s[i])-48; i+=1
    return num,i
def eval2_term(s,i):
    val,i=eval2_factor(s,i)
    while True:
        while i<len(s) and s[i]==' ': i+=1
        if i<len(s) and s[i]=='+':
            i+=1; r,i=eval2_factor(s,i); val+=r
        else: break
    return val,i
def eval2_expr(s,i=0):
    val,i=eval2_term(s,i)
    while True:
        while i<len(s) and s[i]==' ': i+=1
        if i<len(s) and s[i]=='*':
            i+=1; r,i=eval2_term(s,i); val*=r
        else: break
    return val,i
p1=p2=0
for l in lines:
    if not l: continue
    r1,_=eval1(l); r2,_=eval2_expr(l)
    p1+=r1; p2+=r2
print(p1,p2)