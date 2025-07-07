import sys
def main():
    nums=[]
    N=None
    with open(sys.argv[1]) as f:
        for line in f:
            s=line.strip()
            if not s: continue
            if N is None: N=len(s)
            nums.append(int(s,2))
    n_nums=len(nums)
    half=n_nums//2
    gamma=0; epsilon=0
    for i in range(N):
        ones=sum((num>>(N-1-i))&1 for num in nums)
        gamma=(gamma<<1)|(ones>half)
        epsilon=(epsilon<<1)|(ones<=half)
    def rating(prefer_most):
        cand=nums[:]
        for i in range(N):
            if len(cand)==1: break
            ones=sum((num>>(N-1-i))&1 for num in cand)
            zeros=len(cand)-ones
            if prefer_most:
                bit=1 if ones>=zeros else 0
            else:
                bit=0 if zeros<=ones else 1
            cand=[num for num in cand if ((num>>(N-1-i))&1)==bit]
        return cand[0]
    o=rating(True); c=rating(False)
    sys.stdout.write(f"{gamma*epsilon} {o*c}")
if __name__=='__main__':
    main()