from util import model_board, print_board, check_solved, Cell
import copy
 
def solve(board):
    last_board = []  # For stopping in case the board is unsolvable
    state = []
    while not check_solved(board):

        flag = True
        while flag:
            MRV_minimnizing(board)
            flag = sum([1 for i in range(9) for j in range(9) if len(board[i][j].domain) == 1]) != 0


        state = copy.deepcopy(board)
        (i_c, j_c) = [(i, j) for i in range(9) for j in range(9) if len(board[i][j].domain) > 1][0]   #alegem o celula pentru care alegem o valoare din domeniu
        for val in board[i_c][j_c].domain:
            board[i_c][j_c].domain = []
            board[i_c][j_c].final = True
            board[i_c][j_c].value = val
            flag = True
            while flag:
                MRV_minimnizing(board)
                flag = sum([1 for i in range(9) for j in range(9) if len(board[i][j].domain) == 1]) != 0

            if sum([1 for i in range(9) for j in range(9) if len(board[i][j].domain) and not board[i][j].final]) == 0:
                break
            else:
                board = copy.deepcopy(state)

    return board

def MRV_minimnizing(board):
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
    
    for i in range(9):      #pt fiecare cell se transforma 
        for j in range(9):
            if board[i][j].final == False:
                board[i][j].minimize(row_values[i])
                board[i][j].minimize(column_values[j])
                board[i][j].minimize(group_values[(i//3)*3 + j//3])

    return board

array = [
    0,9,0,  8,0,0,  0,0,3,
    0,8,1,  5,0,0,  7,0,0,
    0,0,0,  0,0,0,  5,0,4,

    5,0,0,  0,0,0,  0,0,0,
    0,0,0,  3,1,0,  0,0,0,
    0,0,0,  6,5,0,  4,7,0,

    0,1,6,  0,4,0,  8,0,2,
    9,0,0,  0,0,0,  0,6,0,
    7,0,0,  0,0,9,  0,0,0
]
constraints = [(0,0), (1,0), (2,0), (1,1), 
               (0,3), (0,5), (1,5), (2,4), 
               (0,6), (1,7), (2,7), (2,8), 
               (3,1), (4,0), (4,1), (4,2), 
               (3,3), (5,5), (3,5), (5,3), 
               (3,6), (5,6), (5,8), (4,8), 
               (8,1), (6,2), (7,2), (8,2), 
               (7,3), (6,4), (7,4), (8,4), 
               (6,6), (7,7), (8,7), (6,8) 
               ]

board = model_board(array, constraints)
print_board(board)
result = solve(board)
if result == "Unsolvable":
    print("Sudoku board can not be solved")
else:
    print_board(result)