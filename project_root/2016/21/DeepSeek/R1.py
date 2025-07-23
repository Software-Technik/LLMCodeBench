import sys

class Scrambler:
    def __init__(self, pw):
        self.pw = list(pw)

    def __repr__(self):
        return ''.join(self.pw)

    def swap_positions(self, x_pos, y_pos):
        self.pw[x_pos], self.pw[y_pos] = self.pw[y_pos], self.pw[x_pos]

    def swap_letters(self, x, y):
        idx_x = self.pw.index(x)
        idx_y = self.pw.index(y)
        self.pw[idx_x], self.pw[idx_y] = self.pw[idx_y], self.pw[idx_x]

    def rotate(self, x_pos):
        n = len(self.pw)
        x_pos %= n
        if x_pos:
            self.pw = self.pw[-x_pos:] + self.pw[:-x_pos]

    def rotate_letter(self, x):
        x_pos = self.pw.index(x)
        if x_pos >= 4:
            x_pos += 1
        self.rotate(x_pos + 1)

    def derotate_letter(self, x):
        x_pos = self.pw.index(x)
        if x_pos % 2:
            rot = -((x_pos + 1) // 2)
        elif x_pos:
            rot = (6 - x_pos) // 2
        else:
            rot = -1
        self.rotate(rot)

    def reverse(self, x_pos, y_pos):
        self.pw[x_pos:y_pos+1] = self.pw[x_pos:y_pos+1][::-1]

    def move(self, x_pos, y_pos):
        char = self.pw.pop(x_pos)
        self.pw.insert(y_pos, char)

    def scramble(self, direction=1):
        for instruction in INSTRUCTIONS[::direction]:
            op = instruction[0]
            if op == 'swap':
                if instruction[1] == 'position':
                    self.swap_positions(instruction[2], instruction[3])
                else:
                    self.swap_letters(instruction[2], instruction[3])
            elif op == 'rotate':
                if instruction[1] == 'based':
                    if direction > 0:
                        self.rotate_letter(instruction[2])
                    else:
                        self.derotate_letter(instruction[2])
                else:
                    steps = instruction[2]
                    if instruction[1] == 'left':
                        steps = -steps
                    if direction < 0:
                        steps = -steps
                    self.rotate(steps)
            elif op == 'reverse':
                self.reverse(instruction[1], instruction[2])
            else:
                from_pos, to_pos = instruction[1], instruction[2]
                if direction < 0:
                    from_pos, to_pos = to_pos, from_pos
                self.move(from_pos, to_pos)
        return self

    def unscramble(self):
        return self.scramble(-1)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    lines = infile.read().splitlines()

INSTRUCTIONS = []
for line in lines:
    if not line:
        continue
    parts = line.split()
    if line.startswith('swap'):
        if parts[1] == 'position':
            INSTRUCTIONS.append(('swap', 'position', int(parts[2]), int(parts[5])))
        else:
            INSTRUCTIONS.append(('swap', 'letter', parts[2], parts[5]))
    elif line.startswith('rotate'):
        if parts[1] == 'based':
            INSTRUCTIONS.append(('rotate', 'based', parts[-1]))
        else:
            INSTRUCTIONS.append(('rotate', parts[1], int(parts[2])))
    elif line.startswith('reverse'):
        INSTRUCTIONS.append(('reverse', int(parts[2]), int(parts[4])))
    elif line.startswith('move'):
        INSTRUCTIONS.append(('move', int(parts[2]), int(parts[5])))

plain = 'abcdefgh'
hashed = 'fbgdceah'

first_part = Scrambler(plain).scramble()
second_part = Scrambler(hashed).unscramble()

sys.stdout.write(f"{first_part} {second_part}")