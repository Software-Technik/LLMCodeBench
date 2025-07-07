import sys

class Scrambler:
    def __init__(self, pw):
        self.pw = list(pw)

    def __repr__(self):
        return ''.join(self.pw)

    def swap_positions(self, x_pos, y_pos):
        self.pw[x_pos], self.pw[y_pos] = self.pw[y_pos], self.pw[x_pos]

    def swap_letters(self, x, y):
        self.swap_positions(self.pw.index(x), self.pw.index(y))

    def rotate(self, x_pos):
        x_pos %= len(self.pw)
        self.pw = self.pw[-x_pos:] + self.pw[:-x_pos]

    def rotate_letter(self, x):
        x_pos = self.pw.index(x)
        x_pos = x_pos + 1 + (1 if x_pos >= 4 else 0)
        self.rotate(x_pos)

    def derotate_letter(self, x):
        i = self.pw.index(x)
        for x_pos in range(len(self.pw)):
            if (2 * x_pos + (1 if x_pos >= 4 else 0) + 1) % len(self.pw) == i:
                self.rotate(-x_pos-1)
                return

    def reverse(self, x_pos, y_pos):
        self.pw[x_pos:y_pos+1] = reversed(self.pw[x_pos:y_pos+1])

    def move(self, x_pos, y_pos):
        char = self.pw.pop(x_pos)
        self.pw.insert(y_pos, char)

    def scramble(self, direction=1):
        for instruction in INSTRUCTIONS[::direction]:
            line = instruction.split()
            if instruction.startswith('swap'):
                if line[1] == 'position':
                    self.swap_positions(int(line[2]), int(line[5]))
                else:
                    self.swap_letters(line[2], line[5])
            elif instruction.startswith('rotate'):
                if line[1] == 'based':
                    if direction > 0:
                        self.rotate_letter(line[-1])
                    else:
                        self.derotate_letter(line[-1])
                else:
                    x_pos = int(line[2]) * (-1 if line[1] == 'left' else 1)
                    self.rotate(x_pos * direction)
            elif instruction.startswith('reverse'):
                self.reverse(int(line[2]), int(line[4]))
            elif instruction.startswith('move'):
                x_pos, y_pos = int(line[2]), int(line[5])
                if direction < 0:
                    x_pos, y_pos = y_pos, x_pos
                self.move(x_pos, y_pos)
        return self

    def unscramble(self):
        return self.scramble(-1)

with open(sys.argv[1], 'r') as infile:
    INSTRUCTIONS = infile.read().strip().split('\n')

plain = 'abcdefgh'
hashed = 'fbgdceah'

first_part = Scrambler(plain).scramble()
second_part = Scrambler(hashed).unscramble()

sys.stdout.write(f"{first_part} {second_part}")