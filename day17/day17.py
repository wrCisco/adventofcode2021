#!/usr/bin/env python3


import re
from collections import defaultdict


def run():
    with open('input.txt') as fh:
        target = re.search(r'x=(\d+)\.\.(\d+), y=(-\d+)\.\.(-\d+)', fh.read()).groups()
        target = ((int(target[0]), int(target[1])), (int(target[2]), int(target[3])))

    y_steps = defaultdict(list)
    max_ypos = {}
    for y in range(target[1][0], 200):
        steps = 0
        pos = 0
        velocity = y
        while pos > target[1][1]:
            pos += velocity
            velocity -= 1
            steps += 1
            if velocity >= 0:
                max_ypos[y] = pos
        if target[1][0] <= pos < target[1][1] + 1:
            y_steps[y].append(steps)
        if abs(pos + velocity) <= max(abs(target[1][0]), abs(target[1][1])):
            while pos >= target[1][0]:
                pos += velocity
                velocity -= 1
                steps += 1
                if target[1][0] <= pos < target[1][1] + 1:
                    y_steps[y].append(steps)
    for y in max_ypos.copy():
        if not y_steps.get(y):
            try:
                del max_ypos[y]
            except KeyError:
                pass
    print(max(max_ypos.values()))  # first answer

    x_steps = defaultdict(list)
    x_steps_or_more = {}
    for x in range(target[0][1] + 1):
        steps = 0
        pos = 0
        velocity = x
        while pos < target[0][0] and velocity > 0:
            pos += velocity
            if velocity > 0:
                velocity -= 1
            elif velocity < 0:
                velocity += 1
            steps += 1
        if target[0][0] <= pos < target[0][1] + 1:
            if velocity == 0:
                x_steps_or_more[x] = steps
            else:
                x_steps[x].append(steps)
        if velocity != 0:
            while pos < target[0][1] + 1:
                pos += velocity
                if velocity > 0:
                    velocity -= 1
                elif velocity < 0:
                    velocity += 1
                steps += 1
                if target[0][0] <= pos <= target[0][1]:
                    if velocity == 0:
                        x_steps_or_more[x] = steps
                        break
                    else:
                        x_steps[x].append(steps)
                else:
                    if velocity == 0:
                        break

    max_ysteps = max(max(ysteps) for ysteps in y_steps.values())

    initial_velocities = set()
    for x, xsteps in x_steps.items():
        for y, ysteps in y_steps.items():
            for n in xsteps:
                if n in ysteps:
                    initial_velocities.add((x, y))
    for x, xsteps in x_steps_or_more.items():
        for y, ysteps in y_steps.items():
            for n in range(xsteps, max(ysteps) + 1):
                if n in ysteps:
                    initial_velocities.add((x, y))
    print(len(initial_velocities))  # second answer


if __name__ == '__main__':
    run()
