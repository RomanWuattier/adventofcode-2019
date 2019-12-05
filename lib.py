import sys
import re


OPS = {
    1: { 'params': 3, 'type': '+' }, 
    2: { 'params': 3, 'type': '*' },
    3: { 'params': 1, 'type': 'input' },
    4: { 'params': 1, 'type': 'output' },
    5: { 'params': 2, 'type': 'jump-non-zero' },
    6: { 'params': 2, 'type': 'jump-zero' },
    7: { 'params': 3, 'type': '<' },
    8: { 'params': 3, 'type': '=' },
    99: { 'params': 0, 'type': 'halt' }
}


def internal_intcode(valid_ops, codes):
    VALID_OPS = {op: OPS.get(op) for op in valid_ops}

    output = [None]
    slow_pointer = 0
    
    while slow_pointer < len(codes):
        intcode = codes[slow_pointer]
        opcode = intcode % 100
        
        if opcode not in VALID_OPS:
            print('Invalid opcode: ' + str(opcode))
            break

        op = VALID_OPS.get(opcode)
        if op.get('type') == 'halt':
            break

        fast_pointer = slow_pointer + op.get('params') + 1
        if fast_pointer > len(codes):
            print('Fast pointer > len')
            break

        # To improve. The goal is to manage parameter mode. For example: [1,0,0,2] is interpreted as [0,1,0,0,0]
        modes = [0 for i in range(0, 5)]
        tmp = list(reversed(list(str(intcode))[:-2]))
        for i in range(0, len(tmp)):
            modes[i] = int(tmp[i])
        
        params = [p for p in codes[slow_pointer + 1:fast_pointer]]
        values = [param if mode == 1 else codes[param] for param, mode in list(zip(params, modes))]
        
        jump_to = 0

        if op.get('type') == '+':
            codes[params[-1]] = values[0] + values[1]
        elif op.get('type') == '*':
            codes[params[-1]] = values[0] * values[1]
        elif op.get('type') == 'input':
            codes[params[-1]] = int(input("Input as integer: "))
        elif op.get('type') == 'output':
            output.append(values[-1])
        elif op.get('type') == '<':
            codes[params[-1]] = 1 if values[0] < values[1] else 0
        elif op.get('type') == '=':
            codes[params[-1]] = 1 if values[0] == values[1] else 0
        elif op.get('type') == 'jump-non-zero':
            jump_to = values[1] if values[0] != 0 else 0
        elif op.get('type') == 'jump-zero':    
            jump_to = values[1] if values[0] == 0 else 0

        slow_pointer = jump_to if jump_to > 0 else fast_pointer

    return codes[0], output[-1]


def intcode(codes, noun, verb):
    codes[1] = noun
    codes[2] = verb
    return internal_intcode([1, 2, 99], codes)[0]


def intcode_day5(codes):
    return internal_intcode([1, 2, 3, 4, 5, 6, 7, 8, 99], codes)[1]
