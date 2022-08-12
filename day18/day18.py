#!/usr/bin/env python3


import math


def reduce_number(number):
    explosions, splits = True, True
    while explosions or splits:
        explosions = False
        splits = False
        level = 0
        for i in range(len(number)):
            if number[i] == '[':
                level += 1
            elif number[i] == ']':
                level -= 1
            if level == 5:
                left_explode = number[i+1]
                right_explode = number[i+2]
                li = i
                while li > 0:
                    li -= 1
                    if isinstance(number[li], int):
                        number[li] += left_explode
                        break
                ri = i + 3
                while ri < len(number) - 1:
                    ri += 1
                    if isinstance(number[ri], int):
                        number[ri] += right_explode
                        break
                number[i:i+4] = [0]
                explosions = True
                break
        else:
            for i in range(len(number)):
                if isinstance(number[i], int) and number[i] > 9:
                    digit = number[i]
                    number[i:i+1] = ['[', digit // 2, math.ceil(digit / 2), ']']
                    splits = True
                    break
    return number


def magnitude(number):
    while len(number) > 1:
        i = 1
        while i < len(number) - 1:
            i += 1
            if isinstance(number[i], int) and isinstance(number[i-1], int):
                number[i-2:i+2] = [number[i - 1] * 3 + number[i] * 2]
                i -= 2
    return int(number[0])


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    for i in range(len(lines)):
        lines[i] = list(lines[i])
        lines[i][:] = [c for c in lines[i] if c != ',']
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                lines[i][j] = int(lines[i][j])
    number = lines[0]
    for line in lines[1:]:
        number = reduce_number(['['] + number + line + [']'])
    print(magnitude(number))  # first answer

    max_magnitude = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                n1 = reduce_number(['['] + lines[i] + lines[j] + [']'])
                n2 = reduce_number(['['] + lines[j] + lines[i] + [']'])
                mag = max(magnitude(n1), magnitude(n2))
                if mag > max_magnitude:
                    max_magnitude = mag
    print(max_magnitude)  # second answer
        


if __name__ == '__main__':
    run()
