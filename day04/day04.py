#!/usr/bin/env python3


import re


class Board:

    def __init__(self, rows):
        self.rows = rows
        self.unmarked_sum = sum(map(sum, rows))
        self.nums = { n: (x, y) for y, row in enumerate(self.rows) for x, n in enumerate(row) }

    def mark(self, num):
        coords = self.nums[num]
        del self.nums[num]
        self.unmarked_sum -= num
        self.rows[coords[1]][coords[0]] = -1
        for row in self.rows:
            if sum(row) == -len(row):
                return self.unmarked_sum * num
        columns = list(zip(*self.rows))
        for col in columns:
            if sum(col) == -len(col):
                return self.unmarked_sum * num
        return -1


def play(boards, nums):
    winner = None
    winners = set()
    for num in nums:
        for board in boards:
            if num in board.nums:
                result = board.mark(num)
                if result != -1:
                    if not winner:
                        winner = board
                        print(result)  # first answer
                    winners.add(board)
                    if len(winners) == len(boards):
                        print(result)  # second answer
                        return
        boards -= winners
        winners.clear()


def run():
    with open('input.txt', encoding='utf-8') as fh:
        lines = fh.read().splitlines()

    seq = map(int, lines[0].split(','))
    boards = set()
    rows = []
    for line in lines[1:]:
        if not line:
            if rows:
                boards.add(Board(rows))
            rows = []
        else:
            rows.append([int(num) for num in re.split(r' +', line.strip())])

    play(boards, seq)


if __name__ == '__main__':
    run()
