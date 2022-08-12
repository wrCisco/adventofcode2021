#!/usr/bin/env python3


def move(map_, moves):
    for m in moves:
        old_coords = m[1]
        map_[old_coords] = ['.', map_[old_coords][1], map_[old_coords][2]]
        new_coords = m[2]
        map_[new_coords] = [m[0], map_[new_coords][1], map_[new_coords][2]]


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    map_ = {}
    herdEast = []
    herdSouth = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            nextX = 0 if x == len(lines[0]) - 1 else x + 1
            nextY = 0 if y == len(lines) - 1 else y + 1
            map_[(x, y)] = [lines[y][x], (nextX, y), (x, nextY)]
            if lines[y][x] == '>':
                herdEast.append((x, y))
            elif lines[y][x] == 'v':
                herdSouth.append((x, y))
    steps = 0
    while True:
        moves1 = []
        newHerdEast = []
        for coords in herdEast:
            if map_[map_[coords][1]][0] == '.':
                moves1.append(('>', coords, map_[coords][1]))
                newHerdEast.append(map_[coords][1])
            else:
                newHerdEast.append(coords)
        herdEast = newHerdEast
        move(map_, moves1)
        # for y in range(len(lines)):
        #     for x in range(len(lines[0])):
        #         print(map_[x, y][0], end='')
        #     print('')
        # input()
        moves2 = []
        newHerdSouth = []
        for coords in herdSouth:
            if map_[map_[coords][2]][0] == '.':
                moves2.append(('>', coords, map_[coords][2]))
                newHerdSouth.append(map_[coords][2])
            else:
                newHerdSouth.append(coords)
        herdSouth = newHerdSouth
        move(map_, moves2)
        # for y in range(len(lines)):
        #     for x in range(len(lines[0])):
        #         print(map_[x, y][0], end='')
        #     print('')
        # input()
        steps += 1
        if not moves1 and not moves2:
            break
    print(steps)

if __name__ == '__main__':
    run()
