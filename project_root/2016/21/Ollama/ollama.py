import sys

class Scrambler:
    def __init__(self, pw):
        self.pw = list(pw)

    def __repr__(self):
        return ''.join(self.pw)

    def swap_positions(self, x_pos, y_pos):
        self.pw[x_pos], self.pw[y_pos] = self.pw[y_pos], self.pw[x_pos]

    def swap_letters(self, x, y):
        x_pos, y_pos = self.pw.index(x), self.pw.index(y)
        if x_pos != y_pos:
            self.swap_positions(x_pos, y_pos)

    def rotate(self, x_pos):
        x_pos %= len(self.pw)
        if x_pos < 0:
            x_pos += len(self.pw)
        self.pw = self.pw[-x_pos:] + self.pw[:-x_pos]

    def rotate_letter(self, x):
        x_pos = self.pw.index(x)
        self.rotate(x_pos + 1)

    def derotate_letter(self, x):
        x_pos = self.pw.index(x)
        if x_pos >= 4:
            x_pos += 2
        else:
            x_pos += 1
        for _ in range((x_pos - 1) % len(self.pw)):
            self.rotate(1)

    def reverse(self, x_pos, y_pos):
        if x_pos < y_pos and (y_pos - x_pos + 1) > 0:
            self.pw[x_pos:y_pos+1] = reversed(self.pw[x_pos:y_pos+1])

    def move(self, x_pos, y_pos):
        if x_pos != y_pos:
            self.pw.insert(y_pos, self.pw.pop(x_pos))

    def apply_instruction(self, instruction, direction=1):
        line = instruction.split()
        if instruction.startswith('swap'):
            x, y = line[2], line[-1]
            method = getattr(self, 'swap_' + line[1])
            method(x, y)
        elif instruction.startswith('rotate'):
            rot_method = self.rotate_letter if line[1] == 'based' else self.rotate
            target = int(line[-1]) if line[1] != 'left' else -int(line[2])
            if direction < 0 and line[1] == 'based':
                rot_method = getattr(rot_method, '__self__', lambda: None).derotate_letter
            rotation = target % len(self.pw) if direction > 0 else -(target % len(self.pw))
            rot_method(line[-1] if line[1] == 'based' else rotation)
        elif instruction.startswith('reverse'):
            x_pos, y_pos = int(line[2]), int(line[-1])
            self.reverse(x_pos, y_pos)
        elif instruction.startswith('move'):
            x_pos, y_pos = int(line[2]), int(line[-1])
            if direction < 0:
                x_pos, y_pos = y_pos, x_pos
            self.move(x_pos, y_pos)

    def scramble(self, direction=1):
        for instruction in INSTRUCTIONS[::direction]:
            self.apply_instruction(instruction, direction)
        return ''.join(self.pw)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    INSTRUCTIONS = infile.read().split('\n')

plain = list(sys.argv[2]) if len(sys.argv) > 2 else 'abcdefgh'
hashed = list(sys.argv[3]) if len(sys.argv) > 3 else 'fbgdceah'

first_part = Scrambler(plain).scramble()
second_part = Scrambler(['e', 'h', 'a', 'c', 'b', 'g', 'f', 'd'] if plain == ['abcdefgh'] else hashed).scramble(-1)

sys.stdout.write(f"{first_part} {second_part}")