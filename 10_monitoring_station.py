import sys
import math


# Side note: Every coordinate is inverted:
# asteroid(x, y) is stored as asteroid(y, x), I know...

def asteroid_direction(y, x, dy, dx, asteroids, width, height):
    x += dx
    y += dy
    while x < width and y < height:
        if (y, x) in asteroids:
            return (y, x)
        x += dx
        y += dy
    return None


def discover(future_station, asteroids, width, height):
    asteroids = asteroids.copy()
    asteroids.remove(future_station)

    discovered = set()
    for asteroid in asteroids:
        dx = asteroid[1] - future_station[1]
        dy = asteroid[0] - future_station[0]
        gcd = abs(math.gcd(dx, dy))
        dx = dx // gcd
        dy = dy // gcd
        if (asteroid[0], asteroid[1]) == asteroid_direction(future_station[0], future_station[1], dy, dx, asteroids, width, height):
            discovered.add((dy, dx))
    return discovered


if __name__ == '__main__':
    with open(sys.argv[1]) as puzzle_input:
        asteroid_input = [l.strip() for l in puzzle_input.readlines()]
        height, width = (len(asteroid_input), len(asteroid_input[0]))

        asteroids = set()
        for y in range(0, height):
            for x in range(0, width):
                if asteroid_input[y][x] == '#':
                    asteroids.add((y, x))

        # Part 1
        station_detected = []
        for future_station in asteroids:
            discovered = discover(future_station, asteroids, width, height)
            station_detected.append((len(discovered), future_station, discovered))

        station_detected.sort(reverse=True)
        maximum, station, discovered = station_detected[0]
        print(maximum)

        destroyed = [(math.atan2(dx, dy), (dy, dx)) for dy, dx in discovered]
        destroyed.sort(reverse=True)
        dy, dx = destroyed[200 - 1][1]
        y, x = station[0] + dy, station[1] + dx
        while (y, x) not in asteroids:
            x += dx
            y += dy
        # Part 2
        print(x * 100 + y)
