import sys


DIRECTIONS = {
    'R': [1, 1],
    'L': [1, -1],
    'U': [0, 1],
    'D': [0, -1]
}


def build_wire_segment(wire_segment):
    pos_dist = {}
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
            pos_dist[tuple(pos)] = dist

    return pos_dist


def intersect(wire1, wire2):
    s1 = build_wire_segment(wire1)
    s2 = build_wire_segment(wire2)
    intersections = s1.keys() & s2.keys()
    dists = [(s1.get(i), s2.get(i)) for i in intersections]
    return intersections, dists


if __name__ == '__main__':
    with open(sys.argv[1]) as input:
        wire1, wire2 = [l.split(',') for l in input.readlines()]
        inters = intersect(wire1, wire2)
        print(min([abs(x) + abs(y) for (x, y) in inters[0]]))
        print(min([x + y for (x, y) in inters[1]]))
