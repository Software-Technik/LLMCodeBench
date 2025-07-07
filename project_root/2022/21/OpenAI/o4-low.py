import sys
from collections import deque, defaultdict

def part1(data):
    nums = {}
    ops = {}
    rev = defaultdict(list)
    for line in data:
        k, v = line.split(": ")
        if v.isdigit():
            nums[k] = int(v)
        else:
            x,o,y = v.split()
            ops[k] = (x,o,y)
            rev[x].append(k)
            rev[y].append(k)
    cnt = {k:2 for k in ops}
    dq = deque()
    for k,(x,o,y) in ops.items():
        c = 0
        if x in nums: c+=1
        if y in nums: c+=1
        cnt[k]=2-c
        if cnt[k]==0: dq.append(k)
    while dq:
        k = dq.popleft()
        x,o,y = ops[k]
        a=nums[x]; b=nums[y]
        if o=="+": r=a+b
        elif o=="-": r=a-b
        elif o=="*": r=a*b
        else: r=a//b
        nums[k]=r
        if k=="root": return r
        for m in rev[k]:
            cnt[m]-=1
            if cnt[m]==0: dq.append(m)

def part2(data):
    nums = {}
    ops = {}
    rev = defaultdict(list)
    for line in data:
        k, v = line.split(": ")
        if k=="humn": continue
        if v.isdigit():
            nums[k] = int(v)
        else:
            x,o,y = v.split()
            ops[k] = [x,o,y]
            rev[x].append(k)
            rev[y].append(k)
    cnt = {k:2 for k in ops}
    dq = deque()
    for k,(x,o,y) in ops.items():
        c = (x in nums) + (y in nums)
        cnt[k]=2-c
        if cnt[k]==0: dq.append(k)
    while dq:
        k = dq.popleft()
        x,o,y = ops[k]
        a=nums[x]; b=nums[y]
        if o=="+": r=a+b
        elif o=="-": r=a-b
        elif o=="*": r=a*b
        else: r=a//b
        nums[k]=r
        for m in rev[k]:
            cnt[m]-=1
            if cnt[m]==0: dq.append(m)
    x,o,y = ops["root"]
    if x in nums:
        num=nums[x]; cur=y
    else:
        num=nums[y]; cur=x
    while cur!="humn":
        x,o,y = ops[cur]
        if y in nums:
            b=nums[y]
            if o=="+": num-=b
            elif o=="-": num=b-num
            elif o=="*": num//=b
            else: num=b//num
            cur=x
        else:
            a=nums[x]
            if o=="+": num-=a
            elif o=="-": num+=y and num # unreachable
            elif o=="*": num//=a
            else: num=a//num
            cur=y
    return num

data = [l.strip() for l in open(sys.argv[1])]
print(part1(data))
print(part2(data))