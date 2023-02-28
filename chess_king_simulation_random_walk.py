import numpy as np
import random as rd


def random_move(i, j):
    moves = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1),
             "RU": (-1, 1), "LU": (-1, -1), "RD": (1, 1), "LD": (1, -1)}

    if i == j == 0:
        move = rd.choice([moves[k] for k in ["R", "D", "RD"]])
    elif i == 7 and j == 7:
        move = rd.choice([moves[k] for k in ["L", "U", "LU"]])
    elif i == 0 and j == 7:
        move = rd.choice([moves[k] for k in ["L", "D", "LD"]])
    elif i == 7 and j == 0:
        move = rd.choice([moves[k] for k in ["R", "U", "RU"]])

    elif i == 0 and 1 <= j <= 6:
        move = rd.choice([moves[k] for k in ["R", "D", "L", "RD", "LD"]])

    elif i == 7 and 1 <= j <= 6:
        move = rd.choice([moves[k] for k in ["R", "U", "L", "RU", "LU"]])

    elif 1 <= i <= 6 and j == 0:
        move = rd.choice([moves[k] for k in ["R", "U", "D", "RU", "RD"]])

    elif 1 <= i <= 6 and j == 7:
        move = rd.choice([moves[k] for k in ["L", "U", "D", "LD", "LU"]])
    else:
        move = rd.choice([moves[k] for k in moves])
    return i + move[0], j + move[1]


if __name__ == "__main__":
    board = np.zeros((8, 8), dtype=np.int64)
    iters = 100
    i, j = rd.randint(0, 7), rd.randint(0, 7)

    for _ in range(iters):
        board[i, j] += 1
        i, j = random_move(i, j)

    print(board, end="\n\n")
    board = board / np.sum(board)
    print(board, end="\n\n")