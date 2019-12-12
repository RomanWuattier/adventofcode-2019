import sys
import re
from math import gcd


def apply_step(pos, vels):
    for i, pos_i in enumerate(pos):
        count = 0
        for p in pos:
            if pos_i < p: count += 1
            elif pos_i > p: count -= 1
        vels[i] += count
    
    for i, vel_i in enumerate(vels):
        pos[i] += vel_i


def simulate_moons_motion(moons):
    pos = moons.copy()
    vels = [0] * len(pos)
    for _ in range (0, 1000):
        apply_step(pos, vels)

    return pos, vels


def repeat(moons):
    initial_pos = moons
    pos = moons.copy()
    vels = [0, 0, 0, 0].copy()

    times = 0

    while True:
        apply_step(pos, vels)
        times += 1

        if pos == initial_pos and vels == [0, 0, 0, 0]:
            return times


if __name__ == '__main__':
    with open(sys.argv[1]) as puzzle_input:
        lines = [l for l in puzzle_input.read().split('\n')]
        coordinates = []
        for l in lines:
            coordinates.append([int(d) for d in re.findall(r'-?\d+', l)])

        transpose_x_y_z = [[], [], []]
        for coord in coordinates:
            for i in range(0, len(coord)):
                transpose_x_y_z[i].append(coord[i])

        # Part 1
        pos = []
        vels = []
        for t in transpose_x_y_z:
            p, v = simulate_moons_motion(t)
            pos.append(p), vels.append(v)

        untranspose_pos = [[], [], [], []]
        untranspose_vel = [[], [], [], []]
        for pos, vel in zip(pos, vels):
            for i in range(0, len(pos)):
                untranspose_pos[i].append(pos[i])
                untranspose_vel[i].append(vel[i])

        energy = 0
        for pos, vel in zip(untranspose_pos, untranspose_vel):
            pot = sum(map(abs, pos))
            kin = sum(map(abs, vel))
            energy += pot * kin
        print(energy)

        # Part 2
        times = []
        for t in transpose_x_y_z:
            times.append(repeat(t))

        lcm = times[0]
        for i in times[1:]:
            lcm = int(lcm * i / gcd(lcm, i))
        print(lcm)
