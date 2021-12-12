#!/usr/bin/env python3


from collections import defaultdict


def dfs(caves, cave, visited):
    if cave == 'end':
        return 1
    if cave.islower():
        visited.add(cave)
    total = 0
    for adj in caves[cave]:
        if adj not in visited:
            total += dfs(caves, adj, visited)
    visited.discard(cave)
    return total


def dfs2(caves, cave, visited, visited_twice):
    if cave == 'end':
        return 1
    if cave.islower():
        if cave in visited:
            visited_twice.append(cave)
        visited.add(cave)
    total = 0
    for adj in caves[cave]:
        if adj not in visited or (adj != 'start' and not visited_twice):
            total += dfs2(caves, adj, visited, visited_twice)
    if cave in visited_twice:
        visited_twice.remove(cave)
    else:
        visited.discard(cave)
    return total


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    caves = defaultdict(list)
    for cave1, cave2 in (line.split('-') for line in lines):
        caves[cave1].append(cave2)
        caves[cave2].append(cave1)

    print(dfs(caves, 'start', set()))
    print(dfs2(caves, 'start', set(), []))


if __name__ == '__main__':
    run()
