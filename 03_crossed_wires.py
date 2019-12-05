import sys


DIRECTIONS = {
    'R': [1, 1],
    'L': [1, -1],
    'U': [0, 1],
    'D': [0, -1]
}


def build_wire_segment(wire_segment):
    pos = [0, 0]
    dist = 0
    for segment in wire_segment:
        direction, length = (segment[0], segment[1:])
        if direction not in DIRECTIONS:
            break

        coord, mvt = DIRECTIONS.get(direction)

        for _ in range(0, int(length)):
            pos[coord] += mvt
            dist += 1
            yield tuple(pos), dist


intersection = {}


def intersect(wire1, wire2):
    pos_dist = {}
    for p, d in build_wire_segment(wire1):
        pos_dist[p] = d

    for p, d in build_wire_segment(wire2):
        if p in pos_dist:
            intersection[p] = pos_dist[p] + d


if __name__ == '__main__':
    with open(sys.argv[1]) as input:
        wire1, wire2 = [l.split(',') for l in input.readlines()]
        intersect(wire1, wire2)
        print(min([abs(x) + abs(y) for x, y in intersection]))
        print(min([d for _, d in intersection.items()]))
