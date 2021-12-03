#!/usr/bin/env python3

def most_common_bit(seq, pos):
    return int(sum(int(line[pos]) for line in seq) * 2 >= len(seq))  # in ties wins always 1

def run():
    with open('input.txt', encoding='utf-8') as fh:
        lines = [line.strip() for line in fh.readlines() if line]

    gamma = ''
    epsilon = ''
    for pos in range(len(lines[0])):
        if most_common_bit(lines, pos):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(int(gamma, 2) * int(epsilon, 2))  # first answer

    oxygen_lines = lines.copy()
    co2_lines = lines.copy()
    for pos in range(len(lines[0])):
        mcb = most_common_bit(oxygen_lines, pos)
        oxygen_lines[:] = [line for line in oxygen_lines if int(line[pos]) == mcb]
        mcb = most_common_bit(co2_lines, pos)
        co2_lines[:] = [line for line in co2_lines if int(line[pos]) != mcb] or co2_lines
        # print('after {} cycles, oxygen_lines remaining:\n{}'.format(pos, "\n".join(line for line in oxygen_lines)))
        # print('after {} cycles, co2_lines remaining:\n{}'.format(pos, "\n".join(line for line in co2_lines)))
    print(int(oxygen_lines[0], 2) * int(co2_lines[0], 2))  # second answer


if __name__ == '__main__':
    run()
