from colorama import Fore, init
init(autoreset=True)
import copy
from numpy import dtype

# modelalrea starii initiale sub forma de matrice de tuple tip (valoare, flag)
# flag == true daca poate fi mutat nr valoare
# else flag == false
def model_problem(array):
    matrice = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(9):
        matrice[i // 3][i % 3] = (array[i], False)
        if array[i] == 0:
            i_zero = i // 3
            j_zero = i % 3
    directii = [(i_zero - 1, j_zero), (i_zero + 1, j_zero), (i_zero, j_zero - 1), (i_zero, j_zero + 1)]
    for i, j in directii:
        if 0 <= i < 3 and 0 <= j < 3:
            matrice[i][j] = (matrice[i][j][0], True)
    return matrice

# transformarea matrice de tuple inapoi in vector
def model_back(matrice):
    a = [0,0,0,0,0,0,0,0,0]
    for i in range(3):
        for j in range(3):
            a[i*3+j] = matrice[i][j][0]
    return a

# afisare matrice joc
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print() 

def print_game(matrix):
    for row in matrix:
        for element in row:
            if element[1]:
                color = Fore.GREEN + str(element[0])
                print(color, end=' | ')
            elif element[0] == 0:
                print('0', end=' | ')
            else:
                color = Fore.RED + str(element[0])
                print(color, end=' | ')
        print() 

#verificare daca matricea este egala cu cea initiala
def verificare_stare_finala(matrice):
    array = model_back(matrice)
    array.remove(0)
    if array == sorted(array):
        return True
    else:
        return False

#verificare daca matricea este rezolvata
def verificare_stare_initiala(matrice):
    array = model_back(matrice)
    if array == initial_array:
        return True
    else:
        return False

# returneaza pozitia valorii n din matricea de joc sub forma de tuplu (i,j)
def find_positions(matrice, n):
    for i in range(3):
        for j in range(3):
            if matrice[i][j][0] == n:
                return (i, j)
                      
# returneaza pozitia valorii 0 din matricea de joc
def find_zero(matrice):
    for i in range(3):
        for j in range(3):
            if matrice[i][j][0] == 0:
                return (i, j)

# returneaza valoarea flag-ului (true/false) pt valoarea n
def validare_tranzitie(matrice, n):
    return matrice[find_positions(matrice, n)[0]][find_positions(matrice, n)[1]][1]

# functie care face tranzitia nr n in locul null
def tranzitie(matrice, n):
    if validare_tranzitie(matrice, n) == True:
        m = copy.deepcopy(matrice)
        i = find_positions(matrice, n)[0]
        j = find_positions(matrice, n)[1]

        i0 = find_zero(matrice)[0]
        j0 = find_zero(matrice)[1]

        # actualizarea flag-urilor pt vechile valor care nu mai pot si mutate
        directii = [(i0 - 1, j0), (i0 + 1, j0), (i0, j0 - 1), (i0, j0 + 1)]
        for ii, jj in directii:
            if 0 <= ii < 3 and 0 <= jj < 3 and m[ii][jj][0] != n:
                m[ii][jj] = (m[ii][jj][0], False)

        # actualizare flag-uri pt noile valori care pot fi mutate (vecinii lui n)
        directii = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for ii, jj in directii:
            if 0 <= ii < 3 and 0 <= jj < 3 and m[ii][jj][0] != 0:
                m[ii][jj] = (m[ii][jj][0], True)

        # actualizarea pozitie pt n & null
        m[i0][j0] = (n, False)
        m[i][j] = (0, False)
        return m

    else:
        print("tranzitie nepermisa")

#functie care face parcurgerea miscarilor posibile dupa modelul IDDFS    
def IDDFS_search(matrice, maxSteps):
    nthStepList = [matrice]
    moveList = []
    step = 0
    while step <= maxSteps:
        nextStepList = []
        nextMoveList = []
        step += 1
        for v in nthStepList:
            if verificare_stare_finala(v):
                print("Ajuns la rezolvare prin pasii:")
                print(moveList[nthStepList.index(v)])
                return moveList[nthStepList.index(v)]
        for m in nthStepList:
            for cell in [m[i][j][0] for i in range(3) for j in range(3) if m[i][j][1]]:
                moveMatrix = tranzitie(m, cell)
                if moveMatrix not in nextStepList:
                    nextStepList += [moveMatrix]
                    if moveList != []:
                        list = moveList[nthStepList.index(m)] + [cell]
                        nextMoveList.append(list)
                    else:
                        list = [cell]
                        nextMoveList.append(list)
        #print(nextMoveList)
        #for g in nextStepList:
            #print_game(g)
            #print(nextMoveList[nextStepList.index(g)])
            #print("_______________")
        #print(step)
        nthStepList = copy.deepcopy(nextStepList)
        moveList = copy.deepcopy(nextMoveList)
    print("nu se poate rezolva in nr de miscari")
    return [[(0, False) for i in range(3)] for j in range(3)]


# instanta de joc testata, introdusa sub forma de array
initial_array = [1, 5, 2, 7, 0, 4, 8, 6, 3]  
# initializare matricea de joc
matrix = model_problem(initial_array)

print_game(matrix)
print("______________________")
x=tranzitie(matrix, 5)
print_game(x)
IDDFS_search(matrix, 10)



#867254031
stateList = [7, 1, 3, 5, 6, 4, 2, 0, 8]
matrix = model_problem(stateList)
print_game(matrix)
IDDFS_search(matrix, 25)
