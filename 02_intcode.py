import sys
from lib import intcode


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
