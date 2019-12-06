import sys


# TODO: memoization
def depth(orbit, vertex, d):
    if vertex in orbit.keys():
        d += 1
        return depth(orbit, orbit[vertex], d)
    return d


def bfs_paths(graph, start, goal):
    queue = [(start, [start])] # (vertex, [path])

    while queue:
        (vertex, path) = queue.pop(0)

        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


if __name__ == '__main__':
    with open(sys.argv[1]) as input:
        lines = [l.split(')') for l in input.read().split('\n')]
        
        # Part 1
        orbit = {}
        for (a, b) in lines:
            orbit[b] = a

        print(sum(depth(orbit, vertex, 1) for _, vertex in orbit.items()))

        # Part 2
        graph = {}
        for a, b in lines:
            graph.setdefault(a, set([])).add(b)
            graph.setdefault(b, set([])).add(a)

        print(len(next(bfs_paths(graph, 'YOU', 'SAN'))[1:-1]) - 1)
