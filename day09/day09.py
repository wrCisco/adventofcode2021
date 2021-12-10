#!/usr/bin/env python3


from collections import deque
import math


def is_low_point(x, y, heights):
    h, v = len(heights[0]) - 1, len(heights) - 1
    adj = []
    if (x and not heights[y][x] < heights[y][x-1]) or \
            (y and not heights[y][x] < heights[y-1][x]) or \
            (x != h and not heights[y][x] < heights[y][x+1]) or \
            (y != v and not heights[y][x] < heights[y+1][x]):
        return False
    return True


def adjacents(x, y, heights):
    h, v = len(heights[0]) - 1, len(heights) - 1
    adj = []
    if x:
        adj.append((x-1, y))
    if y:
        adj.append((x, y-1))
    if x != len(heights[0]) - 1:
        adj.append((x+1, y))
    if y != len(heights) - 1:
        adj.append((x, y+1))
    return adj


def run():
    with open('input.txt') as fh:
        heights = [[int(d) for d in line] for line in fh.read().splitlines()]

    low_points = []
    low_coords = []
    for y, line in enumerate(heights):
        for x, height in enumerate(line):
            if is_low_point(x, y, heights):
                low_points.append(height)
                low_coords.append((x, y))

    print(sum(low_points) + len(low_points))  # first answer

    basins = []
    for coords in low_coords:
        basin = {coords}
        edge = {coords}
        while edge:
            pos = edge.pop()
            for adj in adjacents(pos[0], pos[1], heights):
                if heights[adj[1]][adj[0]] < 9 and adj not in basin:
                    basin.add(adj)
                    edge.add(adj)
        basins.append(len(basin))
        if len(basins) > 3:
            basins.remove(min(basins))

    print(math.prod(basins))  # second answer




if __name__ == '__main__':
    run()
