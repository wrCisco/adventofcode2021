#!/usr/bin/env python3


from itertools import product


def flash(x, y, lines, flashes):
    lines[y][x] = -1
    h, v = len(lines[0]) - 1, len(lines) -1
    adj = set(
        product(
            tuple(set((x - 1 if x else x, x, x + 1 if x != h else x))),
            tuple(set((y - 1 if y else y, y, y + 1 if y != v else y)))
        )
    ) - {(x, y)}
    for a in adj:
        if lines[a[1]][a[0]] != -1:
            lines[a[1]][a[0]] += 1
        if lines[a[1]][a[0]] > 9:
            flashes = flash(a[0], a[1], lines, flashes + 1)
    return flashes


def run():
    with open('input.txt') as fh:
        lines = [[int(d) for d in line.strip()] for line in fh]

    flashes = 0
    step = 0
    while True:
        step += 1
        fs = 0
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] != -1:
                    lines[y][x] += 1
                    if lines[y][x] > 9:
                        fs = flash(x, y, lines, fs + 1)
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == -1:
                    lines[y][x] = 0
        flashes += fs
        if step == 100:
            print(flashes)  # first answer
        if fs == len(lines[0]) * len(lines):
            print(step)  # second answer
            break  # I assume the second answer will always come after the first one

        # print(f'After step {step+1}:', '\n'.join(''.join(str(d) for d in line) for line in lines), sep='\n')
        # print(f'flashes: {flashes}')
        # input()


if __name__ == '__main__':
    run()
