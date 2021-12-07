#!/usr/bin/env python3


def run():
    with open('input.txt') as fh:
        crabs = [int(d) for d in fh.read().split(',')]

    fuel = 0
    fuel2a = 0
    fuel2b = 0
    median = sorted(crabs)[len(crabs) // 2]
    mean = sum(crabs) / len(crabs)
    for crab in crabs:
        fuel += abs(median - crab)
        n = abs(int(mean) - crab)
        fuel2a += ((n+1)*n)//2
        n = abs(int(mean + 1) - crab)
        fuel2b += ((n+1)*n)//2
    print(fuel)  # first answer
    print(min(fuel2a, fuel2b))  # second answer


if __name__ == '__main__':
    run()
