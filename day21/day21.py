#!/usr/bin/env python3


from collections import defaultdict


def run():
    with open('input.txt') as fh:
        lines = fh.read().splitlines()

    pos = [int(lines[0][-2:].strip()), int(lines[1][-2:].strip())]
    score = [0, 0]
    move = 6
    turn = 0
    while True:
        p = pos[turn % 2] + int(str(move)[-1])
        if p > 10:
            p -= 10
        pos[turn % 2] = p
        score[turn % 2] += pos[turn % 2]
        if score[turn % 2] >= 1000:
            print(score[(turn + 1) % 2] * (turn + 1) * 3)  # first answer
            break
        move += 9
        turn += 1

    pos = {(int(lines[0][-2:].strip()), int(lines[1][-2:].strip())): {(0, 0): 1}}
    wins = [0, 0]
    three_rolls = { 3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1 }
    delta_universes = {}
    for roll1, univ1 in three_rolls.items():
        for roll2, univ2 in three_rolls.items():
            delta_universes[(roll1, roll2)] = univ1 * univ2
    while pos:
        new_pos = {}
        p1_won = set()
        for move, m_qty in delta_universes.items():
            for p, score in pos.items():
                new_p1 = p[0] + move[0]
                if new_p1 > 10:
                    new_p1 -= 10
                new_p2 = p[1] + move[1]
                if new_p2 > 10:
                    new_p2 -= 10
                for s, s_qty in score.items():
                    if (move[0], p, s) in p1_won:
                        continue
                    new_score1 = s[0] + new_p1
                    new_score2 = s[1] + new_p2
                    if new_score1 >= 21:
                        wins[0] += s_qty * three_rolls[move[0]]
                        p1_won.add((move[0], p, s))
                    elif new_score2 >= 21:
                        wins[1] += s_qty * m_qty
                    else:
                        try:
                            new_pos[(new_p1, new_p2)][(new_score1, new_score2)] += s_qty * m_qty
                        except KeyError:
                            try:
                                new_pos[(new_p1, new_p2)][(new_score1, new_score2)] = s_qty * m_qty
                            except KeyError:
                                new_pos[(new_p1, new_p2)] = {(new_score1, new_score2): s_qty * m_qty}
        pos = new_pos
    print(max(wins))  # second answer



if __name__ == '__main__':
    run()
