import sys
def main():
    lines = open(sys.argv[1]).read().splitlines()
    W, H = 101, 103
    midW, midH = W//2, H//2
    Pxs, Pys, Vxs, Vys = [], [], [], []
    for line in lines:
        left, right = line.split()
        px_str, py_str = left.split(',')
        vx_str, vy_str = right.split(',')
        Pxs.append(int(px_str.split('=')[-1]))
        Pys.append(int(py_str))
        Vxs.append(int(vx_str.split('=')[-1]))
        Vys.append(int(vy_str))
    q1=q2=q3=q4=0
    for Px, Py, Vx, Vy in zip(Pxs, Pys, Vxs, Vys):
        x = (Px + Vx*100) % W
        y = (Py + Vy*100) % H
        if x<midW and y<midH: q1+=1
        if x>midW and y<midH: q2+=1
        if x<midW and y>midH: q3+=1
        if x>midW and y>midH: q4+=1
    part1 = q1*q2*q3*q4
    period = W*H
    vxm = [vx % W for vx in Vxs]
    vym = [vy % H for vy in Vys]
    cur_py = Pxs[:]
    cur_px = Pys[:]
    best = 10**30
    best_t = 0
    n = len(Pxs)
    for t in range(period):
        q1=q2=q3=q4=0
        for rp, cp in zip(cur_px, cur_py):
            if rp<midW and cp<midH: q1+=1
            if rp>midW and cp<midH: q2+=1
            if rp<midW and cp>midH: q3+=1
            if rp>midW and cp>midH: q4+=1
        ans = q1*q2*q3*q4
        if ans<best:
            best = ans
            best_t = t
        for i in range(n):
            cur_py[i] += vxm[i]
            if cur_py[i] >= W: cur_py[i] -= W
            cur_px[i] += vym[i]
            if cur_px[i] >= H: cur_px[i] -= H
    print(part1, best_t)

if __name__ == "__main__":
    main()