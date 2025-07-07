import sys
def knot_logic(lengths,iterations=64):
    nums=list(range(256))
    pos=skip=0
    for _ in range(iterations):
        for l in lengths:
            if l>256:continue
            for i in range(l//2):
                a=(pos+i)&255
                b=(pos+l-1-i)&255
                nums[a],nums[b]=nums[b],nums[a]
            pos=(pos+l+skip)&255
            skip+=1
    return nums
def knot_hash(s):
    lengths=[ord(c) for c in s]+[17,31,73,47,23]
    nums=knot_logic(lengths,64)
    h=[]
    for i in range(0,256,16):
        x=0
        for j in range(i,i+16): x^=nums[j]
        h.append(f"{x:02x}")
    return''.join(h)
with open(sys.argv[1]) as f:
    c=f.read().strip()
lengths=list(map(int,c.split(',')))
r=knot_logic(lengths,1)
print(r[0]*r[1])
print(knot_hash(c))