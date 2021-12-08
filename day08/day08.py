#!/usr/bin/env python3


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    print(
        sum(
            sum(
                len(digit) in (2, 3, 4, 7) for digit in line[61:].split(' ')
            ) for line in lines
        )
    )  # first answer

    tot = 0
    for line in lines:
        nums = {}
        remap = {}
        signals, output = line.split(' | ')
        digits = signals.split(' ')
        for digit in digits.copy():
            if len(digit) in (2, 3, 4, 7):
                if len(digit) == 2:
                    nums[1] = frozenset(digit)
                elif len(digit) == 3:
                    nums[7] = frozenset(digit)
                elif len(digit) == 4:
                    nums[4] = frozenset(digit)
                elif len(digit) == 7:
                    nums[8] = frozenset(digit)
                digits.remove(digit)
        for digit in digits.copy():
            if len(digit) == 5:
                d = frozenset(digit)
                if len(d & nums[7]) == 3:
                    nums[3] = d
                    digits.remove(digit)
        remap['e'] = next(iter(nums[8] - (nums[3] | nums[4])))
        for digit in digits.copy():
            d = frozenset(digit)
            if (nums[3] | nums[4]) == d:
                nums[9] = d
                digits.remove(digit)
            if len(digit) == 5:
                if remap['e'] in digit:
                    nums[2] = frozenset(digit)
                else:
                    nums[5] = frozenset(digit)
                digits.remove(digit)
        remap['c'] = next(iter(nums[2] - nums[5] - {remap['e']}))
        for digit in digits.copy():
            if len(digit) == 6:
                if remap['c'] not in digit:
                    nums[6] = frozenset(digit)
                else:
                    nums[0] = frozenset(digit)
                digits.remove(digit)
        smun = {nums[k]: k for k in nums}
        tot += int(''.join(str(smun[frozenset(d)]) for d in output.split(' ')))
       
    print(tot)  # second answer


if __name__ == '__main__':
    run()
