#!/usr/bin/env python3


def run():
    with open('input.txt') as fh:
        coords, folds = fh.read().split('\n\n')
    
    coords = set(tuple(int(coord) for coord in line.split(',')) for line in coords.splitlines())
    folds = [(line[11], int(line[13:])) for line in folds.splitlines() if line.strip()]
    new_coords = set()
    old_coords = set()
    for i, instr in enumerate(folds):
        if instr[0] == 'x':
            for coord in coords:
                if coord[0] > instr[1]:
                    new_coords.add((coord[0] - (coord[0] - instr[1]) * 2, coord[1]))
                    old_coords.add(coord)
        elif instr[0] == 'y':
            for coord in coords:
                if coord[1] > instr[1]:
                    new_coords.add((coord[0], coord[1] - (coord[1] - instr[1]) * 2))
                    old_coords.add(coord)
        coords |= new_coords
        coords -= old_coords
        new_coords.clear()
        old_coords.clear()
        if not i:
            print(len(coords))  # first answer

    # the second answer is visual
    for y in range(6):
        for x in range(40):
            print('#', end='') if (x, y) in coords else print('.', end='')
        print('\n')


if __name__ == '__main__':
    run()
