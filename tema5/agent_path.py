import copy

def initializare(tabla_joc, poz_curenta, poz_final):
    tabla_joc = [
        [(False, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
        [(False, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
        [(False, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
        [(True, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
        [(False, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
        [(False, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
        [(False, 0), (False, 0), (False, 0), (False, 1), (False, 1), (False, 1), (False, 2), (False, 2), (False, 1), (False, 0)],
    ]

    poz_curenta = (3,0)
    poz_final = (3,7)

