import sys
def main():
    data=open(sys.argv[1]).read().split('\n\n')
    locks=[]; keys=[]
    for block in data:
        rows=block.splitlines()
        if rows[0][0]=='#':
            locks.append(tuple(next(i for i in range(7) if rows[i][j]=='.') for j in range(5)))
        else:
            rev=rows[::-1]
            keys.append(tuple(next(i for i in range(7) if rev[i][j]=='.') for j in range(5)))
    ans=0
    for L in locks:
        for K in keys:
            for a,b in zip(L,K):
                if a+b>7:
                    break
            else:
                ans+=1
    print(ans)
if __name__=='__main__':
    main()