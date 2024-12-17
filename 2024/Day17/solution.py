def solution():
    def get_combo_operand(x, registers):
        if x <= 3:
            return x
        if x == 4:
            return registers[0]
        if x == 5:
            return registers[1]
        if x == 6:
            return registers[2]
        if x == 7:
            return None
    
    with open('./Day17/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    split_idx = data.index("")
    registers = [int(x.split(": ")[1]) for x in data[:split_idx]]
    instructions = [int(x) for x in data[split_idx:][1].removeprefix("Program: ").split(",")]
    
    output = []
    i = 0
    while i + 1 < len(instructions):
        opcode = instructions[i]
        operand = instructions[i + 1]
        combo_operand = get_combo_operand(operand, registers)
        
        if opcode == 0:
            numerator = registers[0]
            denominator = 2**combo_operand
            registers[0] = numerator // denominator
        elif opcode == 1:
            registers[1] ^= operand
        elif opcode == 2:
            registers[1] = combo_operand % 8
        elif opcode == 3 and registers[0] != 0:
            i = operand
            continue
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            output.append(str(combo_operand % 8))
        elif opcode == 6:
            numerator = registers[0]
            denominator = 2**combo_operand
            registers[1] = numerator // denominator
        elif opcode == 7:
            numerator = registers[0]
            denominator = 2**combo_operand
            registers[2] = numerator // denominator

        i += 2

    return ",".join(output)


def solution2():
    def find(program, ans):
        if len(program) == 0:
            return ans
        for x in range(8):
            a = ans << 3 | x
            b = a % 8
            b = b ^ 3
            c = a >> b
            b = (b ^ c)
            b = (b ^ 5)
            # 2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0
            #b = a % 8
            #b = b ^ 3
            #c = a / 2 ^ b # or c = a >> b
            #a = a / 2 ^ 3 # or a = a >> 3 is the only thing where we use the first A, which we need to find out
            #b = b ^ c
            #b = b ^ 5
            #out(b % 8)
            #jump

            if b % 8 == program[-1]:
                sub = find(program[:-1], a)
                if sub is None:
                    continue
                return sub     
            
        return None  
    
    with open('./Day17/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    split_idx = data.index("")
    instructions = [int(x) for x in data[split_idx:][1].removeprefix("Program: ").split(",")]
    
    return find(instructions, 0)
    

if __name__ == "__main__":
    print(solution())
    print(solution2())