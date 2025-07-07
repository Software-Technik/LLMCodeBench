import sys

def main():
    lines = open(sys.argv[1]).read().splitlines()
    instr = []
    n = 8
    for l in lines:
        p = l.split()
        if p[0] == 'swap':
            if p[1] == 'position':
                instr.append(('swap_pos', int(p[2]), int(p[5])))
            else:
                instr.append(('swap_letter', p[2], p[5]))
        elif p[0] == 'rotate' and p[1] in ('left', 'right'):
            s = int(p[2]) % n
            if p[1] == 'left': s = -s
            instr.append(('rotate', s))
        elif p[0] == 'rotate' and p[1] == 'based':
            instr.append(('rotate_based', p[6]))
        elif p[0] == 'reverse':
            instr.append(('reverse', int(p[2]), int(p[4])))
        elif p[0] == 'move':
            instr.append(('move', int(p[2]), int(p[5])))

    def apply(pw, op):
        t = op[0]
        if t == 'swap_pos':
            x, y = op[1], op[2]; pw[x], pw[y] = pw[y], pw[x]
        elif t == 'swap_letter':
            x, y = op[1], op[2]
            i, j = pw.index(x), pw.index(y); pw[i], pw[j] = pw[j], pw[i]
        elif t == 'rotate':
            r = op[1] % n; pw[:] = pw[-r:] + pw[:-r]
        elif t == 'rotate_based':
            x = op[1]; i = pw.index(x)
            r = (1 + i + (i >= 4)) % n; pw[:] = pw[-r:] + pw[:-r]
        elif t == 'reverse':
            x, y = op[1], op[2]; pw[x:y+1] = pw[x:y+1][::-1]
        elif t == 'move':
            x, y = op[1], op[2]; c = pw.pop(x); pw.insert(y, c)

    inv_map = {0:1,1:1,2:6,3:2,4:7,5:3,6:0,7:4}

    def unapply(pw, op):
        t = op[0]
        if t in ('swap_pos', 'swap_letter', 'reverse'):
            apply(pw, op)
        elif t == 'rotate':
            apply(pw, ('rotate', -op[1]))
        elif t == 'rotate_based':
            x = op[1]; j = pw.index(x)
            d = inv_map[j] % n; pw[:] = pw[d:] + pw[:d]
        elif t == 'move':
            apply(pw, ('move', op[2], op[1]))

    pw1 = list('abcdefgh')
    for op in instr: apply(pw1, op)
    pw2 = list('fbgdceah')
    for op in reversed(instr): unapply(pw2, op)
    sys.stdout.write(''.join(pw1) + ' ' + ''.join(pw2))

if __name__ == '__main__':
    main()