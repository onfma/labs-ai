
from colorama import Fore, init
#model problem after an array of known cells along with constraints for even cells
#problem is modeled as a matrix of class structures each having a final value, a boolean if the cell is final or not, same for the even cells and the domain

class Cell:     #structura de celula
    def __init__(self, value, final, even, domain):     #constructor
        self.value = value
        self.final = final
        self.even = even
        self.domain = domain
    
    def minimize(self, array):      #fct care ia un vector de restrictii si minimizeaza domeniul, daca len(dom) == 1 => stare finala
        if self.final:
            return
        
        self.domain = [value for value in self.domain if value not in array]

        if len(self.domain) == 1:
            self.value = self.domain[0]
            self.final = True
            self.domain = []

        return

def model_board(number_array, even_cells):      #modelare ca o matrice de cells
    matrix = []
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_values = [2, 4, 6, 8]
    for i in range(9):
        row = []
        for j in range(9):
            if number_array[i * 9 + j] != 0: 
                row.append(Cell(number_array[i * 9 + j], True, ((i, j) in even_cells), []))

            elif (i, j) in even_cells:
                row.append(Cell(0, False, True, even_values))

            else: 
                row.append(Cell(0, False, False, all_values))
        matrix.append(row)
    return matrix


def print_board(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j].even:
                color = (Fore.GREEN + ' ' + str(matrix[i][j].value) + ' ') if matrix[i][j].final else (Fore.GREEN + ' * ')
                print(color, end='')
            else:
                color = (Fore.WHITE + ' ' + str(matrix[i][j].value) + ' ') if matrix[i][j].final else (Fore.WHITE + ' * ')
                print(color, end='')
            if j%3 == 2:
                print((Fore.WHITE + " | "), end='')
        if i%3 == 2:
            print()
            print((Fore.WHITE +  "____________________________________"))
        else:
            print() 

def check_solved(board):
    unsolved_cells = [board[i][j] for i in range(9) for j in range(9) if board[i][j].final == False]
    return len(unsolved_cells) == 0