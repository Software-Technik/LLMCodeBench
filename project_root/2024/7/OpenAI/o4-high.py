import sys
sys.setrecursionlimit(10000)
def reachable1(nums,target):
    n=len(nums)
    visited=[set() for _ in range(n)]
    def dfs(i,val):
        if val in visited[i]: return False
        visited[i].add(val)
        if i==n-1: return val==target
        x=nums[i+1]
        return dfs(i+1,val+x) or dfs(i+1,val*x)
    return dfs(0,nums[0])
def reachable2(nums,pow10,target):
    n=len(nums)
    visited=[set() for _ in range(n)]
    def dfs(i,val):
        if val in visited[i]: return False
        visited[i].add(val)
        if i==n-1: return val==target
        x=nums[i+1]
        return dfs(i+1,val+x) or dfs(i+1,val*pow10[i+1]+x) or dfs(i+1,val*x)
    return dfs(0,nums[0])
def main():
    ans1=ans2=0
    with open(sys.argv[1]) as f:
        for line in f:
            parts=line.split()
            target=int(parts[0][:-1])
            ss=parts[1:]
            nums=list(map(int,ss))
            pow10=[10**len(s) for s in ss]
            if reachable1(nums,target): ans1+=target
            if reachable2(nums,pow10,target): ans2+=target
    print(ans1,ans2)
if __name__=='__main__':
    main()