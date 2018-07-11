# Sudoku Validator
# A tiny program validating a traditional 9x9 Sudoku.
# Sudoku requires that every row, column and 3x3 square contain
# 1, 2, 3, 4, 5, 6, 7, 8, and 9 numbers. As no duplicates are allowed,
# no rows, columns or regions can be identical.
# The program accepts Python matrix with 9 lists consisting of 9 elements
# as an input.


def done_or_not(board):
    matrix = list(range(1, 10))
    # validating rows
    for row in board:
        if sorted(row) != matrix:
            return "Try again!"
    # validating columns
    for pos in range(len(board)):
        column = []
        for row in board:
            column.append(row[pos])
        if sorted(column) != matrix:
            return "Try again!"
    # validating squares 3x3
    for third in range(0, 9, 3):
        for i in range(1, 4, 1):
            square = []
            for col in range(third, third + 3, 1):
                if i == 1:
                    for row in board[:3]:
                        square.append(row[col])
                if i == 2:
                    for row in board[3:6]:
                        square.append(row[col])
                if i == 3:
                    for row in board[6:9]:
                        square.append(row[col])
            if sorted(square) != matrix:
                return "Try again!"
    return "Finished!"


# test inputs
board = [[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [
    5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 5, 3]]

board2 = [[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [
    5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 3, 5]]


print(done_or_not(board2))
