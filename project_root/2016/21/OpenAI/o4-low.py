import sys

class Scrambler:
    def __init__(self, pw):
        self.pw = pw
    def __repr__(self):
        return ''.join(self.pw)
    def swap_positions(self, x, y):
        self.pw[x], self.pw[y] = self.pw[y], self.pw[x]
    def swap_letters(self, x, y):
        i, j = self.pw.index(x), self.pw.index(y)
        self.pw[i], self.pw[j] = self.pw[j], self.pw[i]
    def rotate(self, n):
        n %= len(self.pw)
        if n:
            self.pw = self.pw[-n:] + self.pw[:-n]
    def rotate_letter(self, x):
        i = self.pw.index(x)
        n = 1 + i + (1 if i >= 4 else 0)
        self.rotate(n)
    def derotate_letter(self, x):
        i = self.pw.index(x)
        if i % 2:
            rot = -(i + 1) // 2
        elif i:
            rot = (6 - i) // 2
        else:
            rot = -1
        self.rotate(rot)
    def reverse(self, x, y):
        self.pw[x:y+1] = reversed(self.pw[x:y+1])
    def move(self, x, y):
        self.pw.insert(y, self.pw.pop(x))
    def scramble(self, instrs):
        for action, a, b in instrs:
            if action == 'swap_pos': self.swap_positions(a, b)
            elif action == 'swap_let': self.swap_letters(a, b)
            elif action == 'rotate': self.rotate(a)
            elif action == 'rotate_pos': self.rotate_letter(a)
            elif action == 'reverse': self.reverse(a, b)
            elif action == 'move': self.move(a, b)
        return self
    def unscramble(self, instrs):
        for action, a, b in reversed(instrs):
            if action == 'swap_pos': self.swap_positions(a, b)
            elif action == 'swap_let': self.swap_letters(a, b)
            elif action == 'rotate': self.rotate(-a)
            elif action == 'rotate_pos': self.derotate_letter(a)
            elif action == 'reverse': self.reverse(a, b)
            elif action == 'move': self.move(b, a)
        return self

path = sys.argv[1]
lines = [l for l in open(path).read().splitlines() if l]
instrs = []
for l in lines:
    p = l.split()
    if p[0]=='swap' and p[1]=='position': instrs.append(('swap_pos', int(p[2]), int(p[5])))
    elif p[0]=='swap': instrs.append(('swap_let', p[2], p[5]))
    elif p[0]=='rotate' and p[1] in ('left','right'):
        n = int(p[2]) * (-1 if p[1]=='left' else 1)
        instrs.append(('rotate', n, None))
    elif p[0]=='rotate': instrs.append(('rotate_pos', p[6], None))
    elif p[0]=='reverse': instrs.append(('reverse', int(p[2]), int(p[4])))
    elif p[0]=='move': instrs.append(('move', int(p[2]), int(p[5])))

plain = list('abcdefgh')
hashed = list('fbgdceah')
first = Scrambler(plain).scramble(instrs)
second = Scrambler(hashed).unscramble(instrs)
sys.stdout.write(f"{first} {second}")