import sys

def part1(lines):
    regs = [int(lines[i].split(':')[1]) for i in range(3)]
    ops = list(map(int, lines[4].split(':',1)[1].split(',')))
    out = []
    p = 0
    n = len(ops)
    while p < n:
        op = ops[p]; v = ops[p+1]
        if op == 0:
            cv = v if v < 4 else regs[v-4]; regs[0] //= 1 << cv
        elif op == 1:
            regs[1] ^= v
        elif op == 2:
            cv = v if v < 4 else regs[v-4]; regs[1] = cv & 7
        elif op == 3:
            if regs[0]:
                p = v; continue
        elif op == 4:
            regs[1] ^= regs[2]
        elif op == 5:
            cv = v if v < 4 else regs[v-4]; out.append(str(cv & 7))
        elif op == 6:
            cv = v if v < 4 else regs[v-4]; regs[1] = regs[0] >> cv
        elif op == 7:
            cv = v if v < 4 else regs[v-4]; regs[2] = regs[0] >> cv
        else:
            raise ValueError(op)
        p += 2
    return ",".join(out)

def part2(lines):
    pr = list(map(int, lines[4].split(':',1)[1].split(',')))
    if pr[-2] != 3 or pr[-1] != 0:
        raise AssertionError
    ln = len(pr) - 2
    def find_solution(target, answer):
        if not target:
            return answer
        for t in range(8):
            a = (answer << 3) | t; b = 0; c = 0; outv = None; adv = False
            for i in range(0, ln, 2):
                op = pr[i]; v = pr[i+1]
                if op == 0:
                    if adv or v != 3: raise ValueError
                    adv = True
                elif op == 1:
                    b ^= v
                elif op == 2:
                    cv = v if v < 4 else (a if v == 4 else b if v == 5 else c); b = cv & 7
                elif op == 3:
                    raise AssertionError
                elif op == 4:
                    b ^= c
                elif op == 5:
                    if outv is not None: raise ValueError
                    cv = v if v < 4 else (a if v == 4 else b if v == 5 else c); outv = cv & 7
                elif op == 6:
                    cv = v if v < 4 else (a if v == 4 else b if v == 5 else c); b = a >> cv
                elif op == 7:
                    cv = v if v < 4 else (a if v == 4 else b if v == 5 else c); c = a >> cv
                else:
                    raise AssertionError
            if outv == target[-1]:
                res = find_solution(target[:-1], a)
                if res is not None:
                    return res
        return None
    return find_solution(pr, 0)

if __name__ == '__main__':
    lines = open(sys.argv[1]).read().splitlines()
    print(part1(lines), part2(lines))