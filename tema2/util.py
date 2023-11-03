
from colorama import Fore, init
import copy
#model problem after an array of known cells along with constraints for even cells
#problem is modeled as a matrix of class structures each having a final value, a boolean if the cell is final or not, same for the even cells and the domain

class Cell:     #structura de celula
    def __init__(self, value, final, even, domain):     #constructor
        self.value = value
        self.final = final #flag true/false
        self.even = even #flag true/false pt constraint
        self.domain = domain #domeniul curent al celulei
        self.first_domain = copy.deepcopy(domain) #domeniul initial folosit pt fc
    
    def minimize(self, array): #scade din domeniu valorile din array
        if self.final:
            return False

        old_dom = self.domain 

        self.domain = [value for value in self.domain if value not in array]

        if len(self.domain) == 1:
            self.value = self.domain[0]  
            self.domain = []
            self.final = True 

        return old_dom == self.domain 

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


def MRV_cell(board): # retrurneaza celula cu cel mai mic domeniu
    min_domain = float('inf')
    cell = None
    for i in range(9):
        for j in range(9):
            cell = (i, j)
            if not board[i][j].final and len(board[i][j].domain) < min_domain:
                min_domain = len(board[i][j].domain)
    return cell

def check_solved(board):
    unsolved_cells = [board[i][j] for i in range(9) for j in range(9) if board[i][j].final == False]
    return len(unsolved_cells) == 0

def check_notSolvable(board): # verifica daca o instanta are celule nefinale cu domeniu vid SAU daca avem 2 valori identice undeva 
    for i in range(9):
        row = [board[i][j].value for j in range(9) if board[i][j].final]
        col = [board[j][i].value for j in range(9) if board[j][i].final]
        grp = [board[j][i].value for j in range(9) if board[j][i].final]
        if any(row.count(x) > 1 for x in row) or any(col.count(x) > 1 for x in col) or any(grp.count(x) > 1 for x in grp):
            return False
        
    if any(board[i][j].value == 0 and len(board[i][j].domain) == 0 for i in range(9) for j in range(9)):
        return False

    return True