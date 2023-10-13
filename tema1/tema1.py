initial_array = [8, 6, 7, 2, 5, 4, 0, 3, 1]

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

matrix = model_problem(initial_array)

def model_back(matrice):
    a = [0,0,0,0,0,0,0,0,0]
    for i in range(3):
        for j in range(3):
            a[i*3+j] = matrice[i][j][0]
    return a

def verificare_stare_finala(matrice):
    array = model_back(matrice)
    array.remove(0)
    if array == sorted(array):
        return True
    else:
        return False

def verificare_stare_initiala(matrice):
    array = model_back(matrice)
    if array == initial_array:
        return True
    else:
        return False

def find_positions(n):
    for i in range(3):
        for j in range(3):
            if matrix[i][j][0] == n:
                return (i, j)
def find_zero():
    for i in range(3):
        for j in range(3):
            if matrix[i][j][0] == 0:
                return (i, j)

def validare_tranzitie(n):
    return matrix[find_positions(n)[0]][find_positions(n)[1]][1]
            
def tranzitie(n):
    if validare_tranzitie(n) == True:
        i = find_positions(n)[0]
        j = find_positions(n)[1]
        aux = matrix[i][j]
        matrix[find_zero[0]][find_zero[1]] = aux
        matrix[i][j] = (0, False)

        



# Exemplu de utilizare
print(matrix)
print(model_back(matrix))
print(verificare_stare_initiala(matrix))
print(verificare_stare_finala(matrix))
