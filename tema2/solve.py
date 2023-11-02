from util import model_board, print_board, check_solved, check_notSolvable, MRV_cell, Cell
import copy

def solve(board):
    while minimizing(board):
        pass

    if not check_notSolvable(board):
        return False
    if check_solved(board):
        return board

    (i, j) = MRV_cell(board)
    cell = board[i][j]

    dom = cell.first_domain
    save_board = [board[i][j] for i in range(9) for j in range(9)]

    for value in dom:
        cell.value = value
        cell.final = True
        cell.domain = []
        board[i][j] = cell  
        if solve(board):
            return True
        board = save_board

    return False


def minimizing(board):
    row_values = []
    column_values = []
    group_values = []
    change = [board[i][j].domain for i in range(9) for j in range(9)]

    for i in range(9):
        row = [board[i][j].value for j in range(9) if board[i][j].final]
        if any(row.count(x) > 1 for x in row):
            return False
        row_values.append(row)

    for j in range(9):
        column = [board[i][j].value for i in range(9) if board[i][j].final]
        if any(column.count(x) > 1 for x in column):
            return False
        column_values.append(column)

    for x in range(3):
        for y in range(3):
            group = [board[i][j].value for i in range(x * 3, x * 3 + 3) for j in range(y * 3, y * 3 + 3) if board[i][j].final]
            if any(group.count(x) > 1 for x in group):
                return False
            group_values.append(group)

    for i in range(9):
        for j in range(9):
            if not board[i][j].final:
                board[i][j].minimize(row_values[i])
                board[i][j].minimize(column_values[j])
                board[i][j].minimize(group_values[(i // 3) * 3 + j // 3])

    return len([(i, j) for i in range(9) for j in range(9) if change[i*9+j] != board[i][j].domain]) != 0
