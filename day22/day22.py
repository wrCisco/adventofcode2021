#!/usr/bin/env python3


from itertools import product


class Cuboid:

    def __init__(self, ranges):
        self.ranges = ranges
        self.area = self.compute_area()

    def x(self):
        return self.ranges[0]

    def y(self):
        return self.ranges[1]
    
    def z(self):
        return self.ranges[2]

    def compute_area(self):
        return abs(self.x().stop - self.x().start) * abs(self.y().stop - self.y().start) * abs(self.z().stop - self.z().start)

    def cubes(self):
        return product(*self.ranges)

    def __str__(self):
        return f'<Cuboid: {self.ranges}>'

    def __repr__(self):
        return f'<Cuboid: {self.ranges}>'

    def __hash__(self):
        return hash(tuple(self.ranges))


def intersection(ranges1, ranges2):
    if (ranges1[0].start >= ranges2[0].stop or ranges1[0].stop <= ranges2[0].start) or \
        (ranges1[1].start >= ranges2[1].stop or ranges1[1].stop <= ranges2[1].start) or \
        (ranges1[2].start >= ranges2[2].stop or ranges1[2].stop <= ranges2[2].start):
        return [range(0), range(0), range(0)]
    r1 = range(max(ranges1[0].start, ranges2[0].start), min(ranges1[0].stop, ranges2[0].stop))
    r2 = range(max(ranges1[1].start, ranges2[1].start), min(ranges1[1].stop, ranges2[1].stop))
    r3 = range(max(ranges1[2].start, ranges2[2].start), min(ranges1[2].stop, ranges2[2].stop))
    return [r1, r2, r3]


def shape_new_cuboids(first, second):
    new_cubes = set()
    if first.x().start < second.x().start:
        new_cubes.add(Cuboid([range(first.x().start, second.x().start), first.y(), first.z()]))
    if first.x().stop > second.x().stop:
        new_cubes.add(Cuboid([range(second.x().stop, first.x().stop), first.y(), first.z()]))
    if first.y().start < second.y().start:
        new_cubes.add(Cuboid([second.x(), range(first.y().start, second.y().start), first.z()]))
    if first.y().stop > second.y().stop:
        new_cubes.add(Cuboid([second.x(), range(second.y().stop, first.y().stop), first.z()]))
    if first.z().start < second.z().start:
        new_cubes.add(Cuboid([second.x(), second.y(), range(first.z().start, second.z().start)]))
    if first.z().stop > second.z().stop:
        new_cubes.add(Cuboid([second.x(), second.y(), range(second.z().stop, first.z().stop)]))
    return new_cubes


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    steps = []
    for line in lines:
        l = line.split(' ')
        action = True if l[0] == 'on' else False
        coords = l[1].split(',')
        ranges = []
        for coord in coords:
            ranges.append(range(int(coord.split('..')[0][2:]), int(coord.split('..')[1]) + 1))
        steps.append([action, Cuboid(ranges)])
    cubes = {}
    for i, step in enumerate(steps[:20]):
        # print(f'executing {i+1}th step...', end=' ')
        for coord in step[1].cubes():
            cubes[coord] = step[0]
        # print(sum(on for on in cubes.values()))
    print(sum(on for on in cubes.values()))  # first answer

    cubes  = set()
    for i, (action, cube) in enumerate(steps):
        new_cubes = set()
        cubes_to_remove = []
        if not i:
            cubes.add(cube)
            continue
        if action:
            new_cubes = {cube}
            for j, other in enumerate(cubes.copy()):
                for k, c in enumerate(new_cubes.copy()):
                    intersect = Cuboid(intersection(c.ranges, other.ranges))
                    if intersect.area:
                        if intersect.x().start == other.x().start and intersect.x().stop == other.x().stop \
                                and intersect.y().start == other.y().start and intersect.y().stop == other.y().stop \
                                and intersect.z().start == other.z().start and intersect.z().stop == other.z().stop:
                                cubes_to_remove.append(other)
                                continue
                        new_cubes.remove(c)
                        if c in cubes:
                            cubes.remove(c)
                        new_cubes.update(shape_new_cuboids(c, intersect))
                cubes.update(new_cubes)
                for o in cubes_to_remove:
                    if o in cubes:
                        cubes.remove(o)
        else:
            new_cubes = set()
            cubes_to_remove = set()
            for j, other in enumerate(cubes.copy()):
                intersect = Cuboid(intersection(cube.ranges, other.ranges))
                if intersect.area:
                    cubes_to_remove.add(other)
                    new_cubes.update(shape_new_cuboids(other, intersect))
            cubes.update(new_cubes)
            for r in cubes_to_remove:
                if r in cubes:
                    cubes.remove(r)

    print(sum(c.area for c in cubes))  # second answer


if __name__ == '__main__':
    run()
