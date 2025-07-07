import sys, math
from itertools import combinations

def can_partition(nums, k, target):
    nums.sort(reverse=True)
    used = [False]*len(nums)
    def dfs(k_rem, start, curr):
        if k_rem == 1: return True
        if curr == target:
            return dfs(k_rem-1, 0, 0)
        prev = None
        for i in range(start, len(nums)):
            if used[i] or nums[i] == prev or curr+nums[i] > target: continue
            used[i] = True
            if dfs(k_rem, i+1, curr+nums[i]):
                return True
            used[i] = False
            prev = nums[i]
            if curr == 0: break
        return False
    return dfs(k, 0, 0)

def solve(groups, packages):
    target = sum(packages)//groups
    packages.sort(reverse=True)
    for r in range(1, len(packages)):
        candidates = []
        for comb in combinations(packages, r):
            if sum(comb) == target:
                candidates.append((math.prod(comb), comb))
        if candidates:
            for qe, comb in sorted(candidates):
                rest = packages.copy()
                for x in comb:
                    rest.remove(x)
                if can_partition(rest, groups-1, target):
                    return qe

data = [int(line) for line in open(sys.argv[1])]
print(solve(3, data))
print(solve(4, data))