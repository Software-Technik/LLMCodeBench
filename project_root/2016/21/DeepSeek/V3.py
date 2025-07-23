import sys

class Scrambler:
    def __init__(self, pw):
        self.pw = list(pw)

    def __repr__(self):
        return ''.join(self.pw)

    def swap_positions(self, x_pos, y_pos):
        self.pw[x_pos], self.pw[y_pos] = self.pw[y_pos], self.pw[x_pos]

    def swap_letters(self, x, y):
        x_pos = self.pw.index(x)
        y_pos = self.pw.index(y)
        self.pw[x_pos], self.pw[y_pos] = self.pw[y_pos], self.pw[x_pos]

    def rotate(self, x_pos):
        x_pos %= len(self.pw)
        if x_pos:
            self.pw = self.pw[-x_pos:] + self.pw[:-x_pos]

    def rotate_letter(self, x):
        x_pos = self.pw.index(x)
        x_pos += 1 + (1 if x_pos >= 4 else 0)
        self.rotate(x_pos)

    def derotate_letter(self, x):
        x_pos = self.pw.index(x)
        if x_pos == 0:
            rot = -1
        elif x_pos % 2 == 1:
            rot = -((x_pos + 1) // 2)
        else:
            rot = (6 - x_pos) // 2
        self.rotate(rot)

    def reverse(self, x_pos, y_pos):
        self.pw[x_pos:y_pos+1] = self.pw[x_pos:y_pos+1][::-1]

    def move(self, x_pos, y_pos):
        char = self.pw.pop(x_pos)
        self.pw.insert(y_pos, char)

    def scramble(self, direction=1):
        instructions = INSTRUCTIONS[::direction]
        for instruction in instructions:
            line = instruction.split()
            if not line:
                continue
            if instruction.startswith('swap'):
                x, y = line[2], line[-1]
                if line[1] == 'position':
                    self.swap_positions(int(x), int(y))
                else:
                    self.swap_letters(x, y)
            elif instruction.startswith('rotate'):
                if line[1] == 'based':
                    if direction > 0:
                        self.rotate_letter(line[-1])
                    else:
                        self.derotate_letter(line[-1])
                else:
                    x_pos = int(line[2])
                    if line[1] == 'left':
                        x_pos *= -1
                    if direction < 0:
                        x_pos *= -1
                    self.rotate(x_pos)
            elif instruction.startswith('reverse'):
                x_pos, y_pos = int(line[2]), int(line[-1])
                self.reverse(x_pos, y_pos)
            elif instruction.startswith('move'):
                x_pos, y_pos = int(line[2]), int(line[-1])
                if direction < 0:
                    x_pos, y_pos = y_pos, x_pos
                self.move(x_pos, y_pos)
        return self

    def unscramble(self):
        return self.scramble(-1)

with open(sys.argv[1], 'r') as infile:
    INSTRUCTIONS = [line.strip() for line in infile if line.strip()]

plain = 'abcdefgh'
hashed = 'fbgdceah'

first_part = Scrambler(plain).scramble()
second_part = Scrambler(hashed).unscramble()

sys.stdout.write(f"{first_part} {second_part}")