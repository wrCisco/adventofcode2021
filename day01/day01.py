#!/usr/bin/env python3


def count_incr(depths):
    return sum(1 for i in range(1, len(depths)) if depths[i] > depths[i-1])

def run():
    with open('input.txt', encoding='utf-8') as fh:
        nums = [int(line.strip()) for line in fh.readlines() if line]

    print(count_incr(nums))  # first answer
    print(
        count_incr(
            [nums[i] + nums[i-1] + nums[i-2] for i in range(2, len(nums))]
        )
    )  # second answer

if __name__ == '__main__':
    run()
