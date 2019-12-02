import sys


VALID_OPS = {
    1: { 'params': 3, 'type': '+' }, 
    2: { 'params': 3, 'type': '*' }, 
    99: { 'params': 0, 'type': 'halt' }
}


def intcode(codes, noun, verb):
    codes[1] = noun
    codes[2] = verb

    slow_pointer = 0
    opcode = codes[slow_pointer]
    while opcode in VALID_OPS:
        op = VALID_OPS.get(opcode)
        if op.get('type') == 'halt':
            break

        fast_pointer = slow_pointer + op.get('params') + 1
        
        param1_addr, param2_addr, out_addr = codes[slow_pointer + 1:fast_pointer]
        param1 = codes[param1_addr]
        param2 = codes[param2_addr]

        if op.get('type') == '+':
            codes[out_addr] = param1 + param2
        elif op.get('type') == '*':
            codes[out_addr] = param1 * param2

        slow_pointer = fast_pointer
        opcode = codes[slow_pointer]

    return codes[0]
    

if __name__ == '__main__':
    with open(sys.argv[1]) as input:
        codes = [int(l) for l in input.read().split(',')]
        # Part 1
        print(intcode(codes.copy(), 12, 2))
        # Part 2
        for noun in range(0, 99):
            for verb in range(0, 99):
                if intcode(codes.copy(), noun, verb) == 19690720:
                    print(100 * noun + verb)
                    break
