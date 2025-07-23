import sys

def part1(lines):
    a = int(lines[0].split(":")[1].strip())
    b = int(lines[1].split(":")[1].strip())
    c = int(lines[2].split(":")[1].strip())
    
    program_line = lines[4].split(":")[1].strip()
    program = [int(value) for value in program_line.split(",")]
    
    output = []
    pointer = 0
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        
        if opcode == 0:
            if operand <= 3:
                val = operand
            elif operand == 4:
                val = a
            elif operand == 5:
                val = b
            elif operand == 6:
                val = c
            else:
                raise ValueError("Invalid operand combo: 7 or more")
            a = a >> val
        elif opcode == 1:
            b ^= operand
        elif opcode == 2:
            if operand <= 3:
                val = operand
            elif operand == 4:
                val = a
            elif operand == 5:
                val = b
            elif operand == 6:
                val = c
            else:
                raise ValueError("Invalid operand combo: 7 or more")
            b = val % 8
        elif opcode == 3:
            if a != 0:
                pointer = operand
                continue
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            if operand <= 3:
                val = operand
            elif operand == 4:
                val = a
            elif operand == 5:
                val = b
            elif operand == 6:
                val = c
            else:
                raise ValueError("Invalid operand combo: 7 or more")
            output.append(str(val % 8))
        elif opcode == 6:
            if operand <= 3:
                val = operand
            elif operand == 4:
                val = a
            elif operand == 5:
                val = b
            elif operand == 6:
                val = c
            else:
                raise ValueError("Invalid operand combo: 7 or more")
            b = a >> val
        elif opcode == 7:
            if operand <= 3:
                val = operand
            elif operand == 4:
                val = a
            elif operand == 5:
                val = b
            elif operand == 6:
                val = c
            else:
                raise ValueError("Invalid operand combo: 7 or more")
            c = a >> val
        else:
            raise ValueError(f"Unknown opcode: {opcode}")
        pointer += 2
        
    return ",".join(output)

def part2(lines):
    program_line = lines[4].split(":")[1].strip()
    program = [int(value) for value in program_line.split(",")]
    
    if program[-2:] != [3, 0]:
        raise AssertionError("Assumption 1: We assume program jumps only once at the end, otherwise we must branch and it becomes too complicated.")
    
    def get_combo_value(operand, a, b, c):
        if operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        raise ValueError("Invalid operand combo: 7 or more")
    
    def find_solution(target, answer):
        if not target:
            return answer
            
        for t in range(8):
            a_val = answer << 3 | t
            b_val = 0
            c_val = 0
            output_val = None
            adv3_encountered = False
            
            for ptr in range(0, len(program)-2, 2):
                opcode = program[ptr]
                operand = program[ptr+1]
                
                if opcode == 0:
                    if adv3_encountered:
                        raise ValueError("Error: Program has multiple ADVs")
                    if operand != 3:
                        raise ValueError("ADV encountered with invalid operand")
                    adv3_encountered = True
                elif opcode == 1:
                    b_val ^= operand
                elif opcode == 2:
                    val = get_combo_value(operand, a_val, b_val, c_val)
                    b_val = val % 8
                elif opcode == 3:
                    raise AssertionError("JNZ found outside expected loop body")
                elif opcode == 4:
                    b_val ^= c_val
                elif opcode == 5:
                    if output_val is not None:
                        raise ValueError("Program has multiple OUT instructions")
                    val = get_combo_value(operand, a_val, b_val, c_val)
                    output_val = val % 8
                elif opcode == 6:
                    val = get_combo_value(operand, a_val, b_val, c_val)
                    b_val = a_val >> val
                elif opcode == 7:
                    val = get_combo_value(operand, a_val, b_val, c_val)
                    c_val = a_val >> val
                else:
                    raise AssertionError(f"Unknown opcode: {opcode}")
            
            if output_val == target[-1]:
                sub_result = find_solution(target[:-1], a_val)
                if sub_result is not None:
                    return sub_result
        return None
        
    return find_solution(program, 0)

input_path = sys.argv[1]

with open(input_path, "r") as file:
    lines = file.readlines()
    print(part1(lines), part2(lines))