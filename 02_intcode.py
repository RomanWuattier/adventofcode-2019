import sys
from intcode import Intcode


if __name__ == '__main__':
    with open(sys.argv[1]) as input:
        codes = [int(l) for l in input.read().split(',')]
        # Part 1
        codes[1] = 12
        codes[2] = 2
        intcode = Intcode(0, codes, [1, 2, 99])
        print(intcode.run()[0])
        # Part 2
        for noun in range(0, 99):
            for verb in range(0, 99):
                codes[1] = noun
                codes[2] = verb
                intcode = Intcode(0, codes, [1, 2, 99])
                if intcode.run()[0] == 19690720:
                    print(100 * noun + verb)
                    break
