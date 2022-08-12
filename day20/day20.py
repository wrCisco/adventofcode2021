#!/usr/bin/env python3


from collections import defaultdict
from itertools import product


def sq(y, x):
    return product((y-1, y, y+1), (x-1, x, x+1))


def print_map(img, x1, y1, x2, y2):
    for y in range(y1, y2):
        print('')
        for x in range(x1, x2):
            print('#' if img[(y, x)] == '1' else '.', end='')
    print('')


def run():
    with open('input.txt') as fh:
        lines = fh.read().split('\n\n')

    ealg = lines[0]
    input_img = lines[1].splitlines()
    image = defaultdict(lambda: '0')
    for y in range(len(input_img)):
        for x in range(len(input_img[0])):
            image[(y, x)] = '1' if input_img[y][x] == '#' else '0'
    minX, minY = -2, -2
    maxX, maxY = len(input_img[0]) + 2, len(input_img) + 2
    for i in range(50):
        if ealg[0] == '.':  # test
            new_img = defaultdict(lambda: '0')
        elif ealg[0] == '#' and ealg[-1] == '.':  # my input
            new_img = defaultdict(lambda: '0' if i % 2 == 0 else '1')
        for y in range(minY, maxY):
            for x in range(minX, maxX):
                n = int(''.join(image[coords] for coords in sq(y, x)), 2)
                new_img[(y, x)] = '1' if ealg[n] == '#' else '0'
        image = new_img
        minX = min(coords[1] for coords in image.keys() if image[coords] == '1') - 2
        minY = min(coords[0] for coords in image.keys() if image[coords] == '1') - 2
        maxX = max(coords[1] for coords in image.keys() if image[coords] == '1') + 3
        maxY = max(coords[0] for coords in image.keys() if image[coords] == '1') + 3
        if i == 1:
            print(sum(pixel == '1' for pixel in image.values()))  # first answer
    print(sum(pixel == '1' for pixel in image.values()))  # second answer


if __name__ == '__main__':
    run()
