import sys


def fuel(mass):
    return int(mass / 3 - 2)


def fuel_of_fuel(mass):
    res = 0
    mass_fuel = fuel(mass)
    while mass_fuel > 0:
        res += mass_fuel
        mass_fuel = fuel(mass_fuel)
    return res


if __name__ == '__main__':
    masses = [int(line.rstrip('\n')) for line in open(sys.argv[1])]
    # Part 1
    print(sum([fuel(mass) for mass in masses]))
    # Part 2
    print(sum([fuel_of_fuel(mass) for mass in masses]))
