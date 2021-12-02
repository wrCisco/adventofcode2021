#!/usr/bin/env python3


def run():
    with open('input.txt', encoding='utf-8') as fh:
        lines = [line.strip().split(' ') for line in fh.readlines() if line]

    pos = 0
    aim = 0
    depth1 = 0
    depth2 = 0
    for line in lines:
        comm, n = line[0], int(line[1])
        if comm == 'forward':
            pos += n
            depth2 += n * aim
        elif comm == 'down':
            depth1 += n
            aim += n
        elif comm == 'up':
            depth1 -= n
            aim -= n

    print(pos * depth1)  # first answer
    print(pos * depth2)  # second answer


if __name__ == '__main__':
    run()
