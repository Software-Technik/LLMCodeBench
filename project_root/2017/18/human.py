import sys
from collections import deque

# Lecture du fichier et nettoyage
input_path = sys.argv[1]
with open(input_path) as f:
    raw_instructions = [line.strip() for line in f if line.strip()]

# Conversion des instructions
instructions = []

for line in raw_instructions:
    if len(line) < 5:
        continue  # ligne trop courte ou invalide
    command = line[1]  # deuxième caractère (unique dans les commandes)
    register = ord(line[4]) - ord('a')
    switch = False
    value = 0
    if len(line) > 5:
        if line[6].isalpha():
            switch = True
            value = ord(line[6]) - ord('a')
        else:
            try:
                value = int(line[6:])
            except ValueError:
                continue  # ligne invalide
    instructions.append((command, switch, register, value))

# Structures de travail
def solve(registers, idx, id='x', first_part=False):
    global x_queue, y_queue, sent_counter
    while idx < len(instructions):
        cmd, switch, r, val = instructions[idx]
        v = registers[val] if switch else val

        if cmd == 'e':  # set
            registers[r] = v
        elif cmd == 'd':  # add
            registers[r] += v
        elif cmd == 'u':  # mul
            registers[r] *= v
        elif cmd == 'o':  # mod
            if v != 0:
                registers[r] %= v
        elif cmd == 'g':  # jgz
            if idx == 33 or registers[r] > 0:
                idx += v
                continue
        elif cmd == 'n':  # snd
            if first_part:
                return registers[r]
            elif id == 'x':
                y_queue.append(registers[r])
            else:
                sent_counter += 1
                x_queue.append(registers[r])
        elif cmd == 'c':  # rcv
            if first_part:
                if registers[r] != 0:
                    return registers[r]
            elif id == 'x' and x_queue:
                registers[r] = x_queue.popleft()
            elif id == 'y' and y_queue:
                registers[r] = y_queue.popleft()
            else:
                return idx
        idx += 1
    return idx

# Initialisation
x_queue = deque()
y_queue = deque()
sent_counter = 0

first_reg = [0] * 26
x_reg = [0] * 26
y_reg = [0] * 26

first_i = x_i = y_i = 0

# Partie 1
print(solve(first_reg, first_i, first_part=True))

# Partie 2
y_reg[ord('p') - ord('a')] = 1
x_i = solve(x_reg, x_i, 'x')
y_i = solve(y_reg, y_i, 'y')

while x_queue or y_queue:
    x_i = solve(x_reg, x_i, 'x')
    y_i = solve(y_reg, y_i, 'y')

print(sent_counter)