import sys
def eval1(s,i):
    n=len(s)
    while i<n and s[i]==' ': i+=1
    if s[i]=='(':
        val,i=eval1(s,i+1);i+=1
    else:
        j=i
        while j<n and s[j].isdigit(): j+=1
        val=int(s[i:j]);i=j
    while True:
        while i<n and s[i]==' ': i+=1
        if i>=n or s[i] not in '+*': break
        op=s[i];i+=1
        while i<n and s[i]==' ': i+=1
        if s[i]=='(':
            rhs,i=eval1(s,i+1);i+=1
        else:
            j=i
            while j<n and s[j].isdigit(): j+=1
            rhs=int(s[i:j]);i=j
        if op=='+': val+=rhs
        else: val*=rhs
    return val,i
def eval2(s,i):
    n=len(s)
    while i<n and s[i]==' ': i+=1
    if s[i]=='(':
        val,i=eval2(s,i+1);i+=1
    else:
        j=i
        while j<n and s[j].isdigit(): j+=1
        val=int(s[i:j]);i=j
    while True:
        while i<n and s[i]==' ': i+=1
        if i>=n or s[i]!='+': break
        i+=1
        while i<n and s[i]==' ': i+=1
        if s[i]=='(':
            rhs,i=eval2(s,i+1);i+=1
        else:
            j=i
            while j<n and s[j].isdigit(): j+=1
            rhs=int(s[i:j]);i=j
        val+=rhs
    while True:
        while i<n and s[i]==' ': i+=1
        if i>=n or s[i]!='*': break
        i+=1
        while i<n and s[i]==' ': i+=1
        if s[i]=='(':
            rhs,i=eval2(s,i+1);i+=1
        else:
            j=i
            while j<n and s[j].isdigit(): j+=1
            rhs=int(s[i:j]);i=j
        val*=rhs
    return val,i
def main():
    lines=open(sys.argv[1]).read().splitlines()
    t1=t2=0
    for line in lines:
        v1,_=eval1(line,0);v2,_=eval2(line,0)
        t1+=v1; t2+=v2
    print(t1, t2)
if __name__=='__main__':
    main()