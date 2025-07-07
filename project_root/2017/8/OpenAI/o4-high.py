import sys,operator
ops={'<':operator.lt,'>':operator.gt,'<=':operator.le,'>=':operator.ge,'==':operator.eq,'!=':operator.ne}
regs={}
regs_get=regs.get
max_ever=-float('inf')
with open(sys.argv[1]) as f:
    for line in f:
        s=line.split()
        if not s: continue
        r,cmd,amt,_,cr,op,val=s
        x=int(amt); y=int(val)
        if ops[op](regs_get(cr,0),y):
            regs[r]=regs_get(r,0)+(x if cmd=='inc' else -x)
            v=regs[r]
            if v>max_ever: max_ever=v
print(max(regs.values()))
print(max_ever)