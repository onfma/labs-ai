from util import model_board, print_board, check_solved, Cell
import copy

def solve(board):
    last_board = []  # For stopping in case the board is unsolvable
    while check_solved(board) == False:

        #adaugat aici area de ales cell si valoare + save state

        row_values = []
        column_values = []
        group_values = []
        for i in range(9):      #lista de valori finale de pe fiecare linie
            row = [board[i][j].value for j in range(9) if board[i][j].final]
            if any(row.count(x) > 1 for x in row):
                return "Unsolvable"
            row_values.append(row)

        for j in range(9):      #--||--- coloana
            column = [board[i][j].value for i in range(9) if board[i][j].final]
            if any(column.count(x) > 1 for x in column):
                return "Unsolvable"
            column_values.append(column)

        for x in range(3):      #--||-- grup de 9
            for y in range(3):
                group = [board[i][j].value for i in range(x * 3, x * 3 + 3) for j in range(y * 3, y * 3 + 3) if board[i][j].final]
                if any(group.count(x) > 1 for x in group):
                    return "Unsolvable"
                group_values.append(group)
        #MRV loop
        for i in range(9):      #pt fiecare cell se transforma 
            for j in range(9):
                if board[i][j].final == False:
                    board[i][j].minimize(row_values[i])
                    board[i][j].minimize(column_values[j])
                    board[i][j].minimize(group_values[(i//3)*3 + j//3])


        #add check pt len(dom) == 0

        #parea asta dispare            
        if board == last_board:
            return "Unsolvable"
        last_board = copy.deepcopy(board)

    return board

