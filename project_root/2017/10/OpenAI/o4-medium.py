import sys
def knot_logic(lengths,iterations,size=256):
    nums=list(range(size))
    pos=0;skip=0
    for _ in range(iterations):
        for l in lengths:
            if l>size: continue
            for i in range(l//2):
                a=(pos+i)%size; b=(pos+l-1-i)%size
                nums[a],nums[b]=nums[b],nums[a]
            pos=(pos+l+skip)%size; skip+=1
    return nums

def knot_hash(s):
    lengths=[*map(ord,s.strip())]+[17,31,73,47,23]
    nums=knot_logic(lengths,64)
    h=[]
    for i in range(0,256,16):
        x=nums[i]
        for y in nums[i+1:i+16]: x^=y
        h.append(f'{x:02x}')
    return ''.join(h)

data=open(sys.argv[1]).read().strip()
l1=list(map(int,data.split(',')))
n1=knot_logic(l1,1)
print(n1[0]*n1[1])
print(knot_hash(data))