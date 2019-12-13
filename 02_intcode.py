import sys
from intcode import Intcode


puzzle_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]


if __name__ == '__main__':
    codes = puzzle_input
    # Part 1
    codes[1] = 12
    codes[2] = 2
    intcode = Intcode(0, codes, [1, 2, 99])
    print(intcode.run().get_first_code())
    # Part 2
    for noun in range(0, 99):
        for verb in range(0, 99):
            codes[1] = noun
            codes[2] = verb
            intcode = Intcode(0, codes, [1, 2, 99])
            if intcode.run().get_first_code() == 19690720:
                print(100 * noun + verb)
                break
