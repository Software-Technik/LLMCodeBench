import sys
import functools

def part(text, repeat):
    lines = text.strip().splitlines()
    total = 0
    for line in lines:
        s, gs = line.strip().split()
        lookup = {"#":2,"?":1,".":0}
        data0 = tuple(lookup[c] for c in s)
        blocks0 = tuple(map(int, gs.split(",")))
        data = (data0 * repeat)[:len(data0)*repeat-1]
        data += (1,)
        blocks = blocks0 * repeat
        n = len(data)
        m = len(blocks)
        sumBlocks = [0]*(m+1)
        for i in range(m-1, -1, -1):
            sumBlocks[i] = sumBlocks[i+1] + blocks[i]
        suffix_min = [0]*(n+1)
        suffix_max = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix_min[i] = suffix_min[i+1] + (data[i]==2)
            suffix_max[i] = suffix_max[i+1] + (data[i]>0)
        @functools.lru_cache(None)
        def dfs(i,k):
            total_b = sumBlocks[k]
            if suffix_min[i] > total_b or suffix_max[i] < total_b: return 0
            if total_b == 0: return 1
            if i>=n: return 0
            d = data[i]
            if d==0:
                return dfs(i+1,k)
            if d==2:
                l = blocks[k]
                if i+l<=n and all(data[i+j]>0 for j in range(l)) and (i+l==n or data[i+l]<2):
                    if i+l==n: return 1
                    return dfs(i+l+1,k+1)
                return 0
            # d==1
            # skip
            res = dfs(i+1,k)
            # treat as 2
            l = blocks[k]
            if i+l<=n and all((data[i+j]>0 if j>0 else True) for j in range(l)) and (i+l==n or data[i+l]<2):
                if i+l==n:
                    res += 1
                else:
                    res += dfs(i+l+1,k+1)
            return res
        total += dfs(0,0)
    return total

text = open(sys.argv[1]).read()
print(part(text,1), part(text,5))