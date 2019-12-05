#!/usr/bin/python3

import utilities

DIRECTION_VECTORS = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def main():
    data = utilities.data(3)
    lines =  data.split('\n')
    path1 = lines[0].split(',')
    path2 = lines[1].split(',')


    points_visited = {}
    intersections = set()

    cursor = (0, 0)
    vector = (0, 0)
    distance_travelled = 0

    for instruction in path1:
        direction = instruction[0]
        distance = int(instruction[1:])

        vector = DIRECTION_VECTORS[direction]

        for i in range(distance):
            distance_travelled += 1
            cursor = tuple(map(sum, zip(cursor, vector)))
            (x, y) = cursor
            if x not in points_visited:
                points_visited[x] = {}
            if y not in points_visited[x]:
                points_visited[x][y] = distance_travelled


            points_visited[cursor] = (cursor[0], cursor[1], distance_travelled)


    cursor = (0, 0)
    distance_travelled = 0

    for instruction in path2:
        direction = instruction[0]
        distance = int(instruction[1:])

        vector = DIRECTION_VECTORS[direction]

        for i in range(distance):
            cursor = tuple(map(sum, zip(cursor, vector)))
            distance_travelled += 1
            (x, y) = cursor

            if x in points_visited:
                if y in points_visited[x]:
                    prev_dist = points_visited[x][y]
                    intersections.add((cursor[0], cursor[1], prev_dist + distance_travelled))

    solution = min([abs(point[0]) + abs(point[1]) for point in intersections])
    print(solution)

    print(min([point[2] for point in intersections]))


if __name__ == '__main__':
    main()
