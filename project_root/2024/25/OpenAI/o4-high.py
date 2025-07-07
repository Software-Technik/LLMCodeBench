import sys
locks=[]
keys=[]
ans=0
buf=[]
with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        if not line: continue
        buf.append(line)
        if len(buf)<7: continue
        first=buf[0][0]
        vs=[0,0,0,0,0]
        if first=='#':
            for j in range(5):
                for i in range(7):
                    if buf[i][j]=='.':
                        vs[j]=i
                        break
            for kv in keys:
                if vs[0]+kv[0]<=7 and vs[1]+kv[1]<=7 and vs[2]+kv[2]<=7 and vs[3]+kv[3]<=7 and vs[4]+kv[4]<=7:
                    ans+=1
            locks.append(vs)
        else:
            for j in range(5):
                for i in range(6,-1,-1):
                    if buf[i][j]=='.':
                        vs[j]=6-i
                        break
            for lv in locks:
                if vs[0]+lv[0]<=7 and vs[1]+lv[1]<=7 and vs[2]+lv[2]<=7 and vs[3]+lv[3]<=7 and vs[4]+lv[4]<=7:
                    ans+=1
            keys.append(vs)
        buf.clear()
print(ans)