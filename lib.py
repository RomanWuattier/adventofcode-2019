class Intcode:

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

    
    def __init__(self, id, codes, valid_ops):
        self.id = id
        self.codes = codes.copy()
        self.valid_ops = {op: self.OPS.get(op) for op in valid_ops}
        self.halt = False
        self.stop = False
        self.output = [None]
        self.slow_pointer = 0
        self.phase = 0


    def getId(self):
        return self.id


    def halted(self) :
        return self.halt


    def intcode(self, instructions = []):
        self.stop = False

        while self.slow_pointer < len(self.codes) and not self.stop:
            intcode = self.codes[self.slow_pointer]
            opcode = intcode % 100

            op = self.valid_ops.get(opcode)
            if op.get('type') == 'halt':
                self.halt = True
                break

            fast_pointer = self.slow_pointer + op.get('params') + 1
            if fast_pointer > len(self.codes):
                print('Fast pointer > len')
                break

            # To improve. The goal is to manage parameter mode. For example: [1,0,0,2] is interpreted as [0,1,0,0,0]
            modes = [0 for i in range(0, 5)]
            tmp = list(reversed(list(str(intcode))[:-2]))
            for i in range(0, len(tmp)):
                modes[i] = int(tmp[i])

            params = [p for p in self.codes[self.slow_pointer + 1:fast_pointer]]
            values = [param if mode == 1 else self.codes[param] for param, mode in list(zip(params, modes))]

            jump_to = 0

            if op.get('type') == '+':
                self.codes[params[-1]] = values[0] + values[1]
            elif op.get('type') == '*':
                self.codes[params[-1]] = values[0] * values[1]
            elif op.get('type') == 'input':
                if len(instructions) > 0:
                    self.codes[params[-1]] = instructions.pop(0)
                else:
                    print('Input opcode unsupported')
                    self.stop = True
            elif op.get('type') == 'output':
                self.stop = True
                self.output.append(values[-1])
            elif op.get('type') == '<':
                self.codes[params[-1]] = 1 if values[0] < values[1] else 0
            elif op.get('type') == '=':
                self.codes[params[-1]] = 1 if values[0] == values[1] else 0
            elif op.get('type') == 'jump-non-zero':
                jump_to = values[1] if values[0] != 0 else 0
            elif op.get('type') == 'jump-zero':    
                jump_to = values[1] if values[0] == 0 else 0
            else:
                print('Invalid opcode: ' + str(opcode))

            self.slow_pointer = jump_to if jump_to > 0 else fast_pointer

        return self.codes[0], self.output[-1]
