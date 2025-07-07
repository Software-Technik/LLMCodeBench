import sys


def part1(lines):
    registers = {
        "A": int(lines[0].split(":")[1].strip()),
        "B": int(lines[1].split(":")[1].strip()),
        "C": int(lines[2].split(":")[1].strip()),
    }

    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers["A"]
        elif operand == 5:
            return registers["B"]
        elif operand == 6:
            return registers["C"]
        else:
            raise ValueError("Invalid operand combo")

    output = []
    pointer = 0
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:
            registers["A"] //= 2 ** get_combo_value(operand)
        elif opcode == 1:
            registers["B"] ^= operand
        elif opcode == 2:
            registers["B"] = get_combo_value(operand) % 8
        elif opcode == 3:
            if registers["A"] != 0:
                pointer = operand
                continue
        elif opcode == 4:
            registers["B"] ^= registers["C"]
        elif opcode == 5:
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:
            registers["B"] = registers["A"] // 2 ** get_combo_value(operand)
        elif opcode == 7:
            registers["C"] = registers["A"] // 2 ** get_combo_value(operand)
        else:
            raise ValueError("Unknown opcode")

        pointer += 2

    return ",".join(map(str, output))


def part2(lines):
    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

    if program[-2:] != [3, 0]:
        raise AssertionError("Unexpected program end")

    def get_combo_value(operand, registers):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return registers["A"]
        if operand == 5:
            return registers["B"]
        if operand == 6:
            return registers["C"]
        raise ValueError("Invalid operand combo")

    def find_solution(target, answer):
        if not target:
            return answer

        for t in range(8):
            registers = {"A": answer << 3 | t, "B": 0, "C": 0}
            output = None
            adv3_encountered = False

            for pointer in range(0, len(program) - 2, 2):
                opcode = program[pointer]
                operand = program[pointer + 1]

                if opcode == 0:
                    if adv3_encountered:
                        raise ValueError("Multiple ADVs")
                    if operand != 3:
                        raise ValueError("Invalid ADV")
                    adv3_encountered = True

                elif opcode == 1:
                    registers["B"] ^= operand
                elif opcode == 2:
                    registers["B"] = get_combo_value(operand, registers) % 8
                elif opcode == 3:
                    raise AssertionError("Unexpected JNZ")
                elif opcode == 4:
                    registers["B"] ^= registers["C"]
                elif opcode == 5:
                    if output is not None:
                        raise ValueError("Multiple OUTs")
                    output = get_combo_value(operand, registers) % 8
                elif opcode == 6:
                    registers["B"] = registers["A"] >> get_combo_value(operand, registers)
                elif opcode == 7:
                    registers["C"] = registers["A"] >> get_combo_value(operand, registers)
                else:
                    raise AssertionError("Unknown opcode")

            if output == target[-1]:
                sub_result = find_solution(target[:-1], registers["A"])
                if sub_result is not None:
                    return sub_result

        return None

    solution = find_solution(program, 0)
    return solution


input_path = sys.argv[1]

with open(input_path, "r") as file:
    lines = file.readlines()

print(part1(lines), part2(lines))