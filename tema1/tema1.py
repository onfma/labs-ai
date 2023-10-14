# instanta de joc testata, introdusa sub forma de array
initial_array = [8, 6, 7, 2, 5, 4, 0, 3, 1]

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

# initializare matricea de joc
matrix = model_problem(initial_array)


# transformarea matrice de tuple inapoi in vector
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


# returneaza pozitia valorii n din matricea de joc sub forma de tuplu (i,j)
def find_positions(n):
    for i in range(3):
        for j in range(3):
            if matrix[i][j][0] == n:
                return (i, j)
                      
# returneaza pozitia valorii 0 din matricea de joc
def find_zero():
    for i in range(3):
        for j in range(3):
            if matrix[i][j][0] == 0:
                return (i, j)


# returneaza valoarea flag-ului (true/false) pt valoarea n
def validare_tranzitie(n):
    return matrix[find_positions(n)[0]][find_positions(n)[1]][1]

# functie care face tranzitia nr n in locul null
def tranzitie(matrice, n):
    if validare_tranzitie(n) == True:
        i = find_positions(n)[0]
        j = find_positions(n)[1]

        i0 = find_zero()[0]
        j0 = find_zero()[1]

        # actualizarea flag-urilor pt vechile valor care nu mai pot si mutate
        directii = [(i0 - 1, j0), (i0 + 1, j0), (i0, j0 - 1), (i0, j0 + 1)]
        for ii, jj in directii:
            if 0 <= ii < 3 and 0 <= jj < 3 and matrice[ii][jj][0] != n:
                matrice[ii][jj] = (matrice[ii][jj][0], False)

        # actualizare flag-uri pt noile valori care pot fi mutate (vecinii lui n)
        directii = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for ii, jj in directii:
            if 0 <= ii < 3 and 0 <= jj < 3 and matrice[ii][jj][0] != 0:
                matrice[ii][jj] = (matrice[ii][jj][0], True)

        # actualizarea pozitie pt n & null
        matrice[i0][j0] = (n, False)
        matrice[i][j] = (0, False)

    else:
        print("tranzitie nepermisa")
        
        

# afisare matrice joc
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()  # Trecem la următorul rând

tranzitie(matrix, 3)
print_matrix(matrix)


