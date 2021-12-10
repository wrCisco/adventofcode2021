#!/usr/bin/env python3


from functools import reduce


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    matches = { '(': ')', '[': ']', '{': '}', '<': '>' }
    points1 = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    points2 = { ')': 1, ']': 2, '}': 3, '>': 4 }
    score1 = 0
    score2 = []
    for line in lines:
        opened = []
        for char in line:
            if char in points1:
                # there are always opening braces before closing ones in input
                if char != matches[opened.pop()]:
                    score1 += points1[char]
                    break
            else:
                opened.append(char)
        else:
            autocomplete = [matches[c] for c in reversed(opened)]
            score2.append(reduce(lambda x, y: x * 5 + points2[y], autocomplete, 0))
    print(score1)  # first answer
    print(sorted(score2)[len(score2) // 2])  # second answer


if __name__ == '__main__':
    run()
