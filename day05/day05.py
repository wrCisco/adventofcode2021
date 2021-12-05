#!/usr/bin/env python3


from collections import Counter


def run():
    with open('input.txt', encoding='utf-8') as fh:
        lines = [line.strip().split(' -> ') for line in fh.readlines() if line]

    for i in range(len(lines)):
        for n in range(2):
            lines[i][n] = [int(d) for d in lines[i][n].split(',')]

    occupied = Counter()
    occupied2 = Counter()
    for s, e in lines:
        if s[1] == e[1]:
            for n in range(min(s[0], e[0]), max(s[0], e[0])+1):
                occupied[(n, s[1])] += 1
        elif s[0] == e[0]:
            for n in range(min(s[1], e[1]), max(s[1], e[1])+1):
                occupied[(s[0], n)] += 1
        else:
            if s[0] > e[0]:
                dx = range(s[0], e[0]-1, -1)
            else:
                dx = range(s[0], e[0]+1)
            if s[1] > e[1]:
                dy = iter(range(s[1], e[1]-1, -1))
            else:
                dy = iter(range(s[1], e[1]+1))
            for x in dx:
                occupied2[(x, next(dy))] += 1

    print(sum(occupied[point] >= 2 for point in occupied))  # first answer
    occupied += occupied2
    print(sum(occupied[point] >= 2 for point in occupied))  # second answer


if __name__ == '__main__':
    run()
