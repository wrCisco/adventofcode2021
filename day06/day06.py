#!/usr/bin/env python3


from collections import Counter


def run():
    with open('input.txt') as fh:
        fish = Counter(int(d) for d in fh.read().split(','))

    for day in range(256):
        new_fish = Counter()
        for k, v in fish.items():
            if k not in (0, 7):
                new_fish[k-1] = v
            elif k == 0:
                new_fish[6] = v + fish[7]
                new_fish[8] = v
            elif k == 7:
                new_fish[6] = v + fish[0]
        fish = new_fish
        if day == 79:
            print(sum(fish.values()))  # first answer
    print(sum(fish.values()))  # second answer


if __name__ == '__main__':
    run()
