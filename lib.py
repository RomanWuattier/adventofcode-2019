OPS = {
    1: { 'params': 3, 'type': '+' }, 
    2: { 'params': 3, 'type': '*' },
    3: { 'params': 1, 'type': 'input' },
    4: { 'params': 1, 'type': 'output' },
    99: { 'params': 0, 'type': 'halt' }
}


def internal_intcode(valid_ops, codes):
    VALID_OPS = {op: OPS.get(op) for op in valid_ops}

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


def intcode(codes, noun, verb):
    codes[1] = noun
    codes[2] = verb
    return internal_intcode([1, 2, 99], codes)
