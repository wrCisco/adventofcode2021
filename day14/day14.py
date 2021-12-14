#!/usr/bin/env python3

from collections import Counter

def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    template = lines[0]
    pairs = Counter()
    for i in range(len(template) - 1):
        pairs[f'{template[i]}{template[i+1]}'] += 1
    rules = {}
    for rule in lines[2:]:
        rules[rule[:2]] = (f'{rule[0]}{rule[-1]}', f'{rule[-1]}{rule[1]}')

    letters = Counter(l for l in template)
    for i in range(40):
        p = pairs.copy()
        for pair in p:
            if p[pair]:
                pairs[pair] -= p[pair]
                pairs[rules[pair][0]] += p[pair]
                pairs[rules[pair][1]] += p[pair]
                letters[rules[pair][0][-1]] += p[pair]
        if i == 9:
            print(max(letters.values()) - min(letters.values()))  # first answer
    print(max(letters.values()) - min(letters.values()))  # second answer

if __name__ == '__main__':
    run()
