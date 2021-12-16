#!/usr/bin/env python3


import networkx as nx


def build_graph(map_):
    g = nx.DiGraph()
    for y, line in enumerate(map_):
        for x, col in enumerate(line):
            if x:
                g.add_edge((x, y), (x - 1, y), weight=map_[y][x - 1])
            if y:
                g.add_edge((x, y), (x, y - 1), weight=map_[y - 1][x])
            if x != len(line) - 1:
                g.add_edge((x, y), (x + 1, y), weight=map_[y][x + 1])
            if y != len(map_) - 1:
                g.add_edge((x, y), (x, y + 1), weight=map_[y + 1][x])
    return g


def run():
    with open('input.txt') as fh:
        lines = [[int(d) for d in line.strip()] for line in fh]

    g = build_graph(lines)

    path = nx.dijkstra_path(g, (0, 0), (len(lines[0]) - 1, len(lines) - 1))
    print(sum(g.edges[path[i], path[i + 1]]['weight'] for i in range(len(path) - 1)))  # first answer

    newmap = []
    for y in range(len(lines) * 5):
        offset_y = y // len(lines)
        newmap.append([])
        for x in range(len(lines[0] * 5)):
            offset_x = x // len(lines[0])
            w = lines[y % len(lines)][x % len(lines[0])] + offset_y + offset_x
            if w >= 10:
                w = w % 10 + 1
            newmap[-1].append(w)
    # print('\n'.join(''.join(str(d) for d in line) for line in newmap))
    
    g = build_graph(newmap)

    path = nx.dijkstra_path(g, (0, 0), (len(newmap[0]) - 1, len(newmap) - 1))
    print(sum(g.edges[path[i], path[i + 1]]['weight'] for i in range(len(path) - 1)))  # second answer


if __name__ == '__main__':
    run()
