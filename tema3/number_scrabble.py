from itertools import combinations
import copy
import random

def initializare(player):
    if player != 1 and player != 2:
        raise ValueError("player trebuie să fie fie 1 sau 2")

    state = {
        "player": player, # e randul player sa aleaga un nou nr
        "n1": {"owner": 0, "valoare": 0},
        "n2": {"owner": 0, "valoare": 0},
        "n3": {"owner": 0, "valoare": 0},
        "n4": {"owner": 0, "valoare": 0},
        "n5": {"owner": 0, "valoare": 0},
        "n6": {"owner": 0, "valoare": 0},
        "n7": {"owner": 0, "valoare": 0},
        "n8": {"owner": 0, "valoare": 0},
        "n9": {"owner": 0, "valoare": 0},
    }

    return state

def verificare_win(state, player):
    # verifica daca in nr alese de player exista o combo de 3 cu suma 15
    list_numbers = [state[f"n{i}"]["valoare"] for i in range(1, 10) if state[f"n{i}"]["owner"] == player]
    for combo in combinations(list_numbers, 3):
        if sum(combo) == 15:
            return True
    return False

def verificare_stare_finala(state):
    # player 1 catiga
    if verificare_win(state, 1): return 1 
    # player 2 castiga
    elif verificare_win(state, 2): return 2 
    # tie
    elif all(state[f"n{i}"]["owner"] != 0 for i in range(1, 10)): return 3 
    # not finished
    else: return 4 

def validare_tranzitie(state, value):
    if 1 <= value < 10:
        for i in range(1, 10):
            if state[f"n{i}"]["valoare"] == value:
                return False
        return True
    return False

def tranzitie(state, value):
    for i in range(1, 10):
        if state[f"n{i}"]["owner"] == 0: # gaseste primul set neasignat
            state[f"n{i}"]["valoare"] = value
            state[f"n{i}"]["owner"] = state["player"]
            state["player"] = 3 - state["player"]  # schimbă jucătorul curent
            break

def euristica(state, available_numbers):
    # calculam cate posibilitati de combinatii castigatoare are jucatorul advers pt urmatoarea sa mutare
    opponent = 3 - state["player"]
    opponent_values = []
    count = 0
    val = None

    for i in range(1, 10):
        if state[f"n{i}"]["owner"] == opponent:
            opponent_values.append(int(state[f"n{i}"]["valoare"]))

    for i in available_numbers:
        opponent_values.append(i)
        for combo in combinations(opponent_values, 3):
            if sum(combo) == 15:
                count = count + 1
                val = i
        opponent_values.remove(i)

    return count, val

def minimax(state, depth, available_numbers):

    if verificare_stare_finala(state) == True or depth == 0:
        return euristica(state, available_numbers)
    
    # computer
    if state["player"] == 2: 
        best_scor = float('-inf') # plus infinit pt a gasi mini
        best_value = None

        for n in available_numbers:
            new_state = copy.deepcopy(state)
            if validare_tranzitie(new_state,n):
                tranzitie(new_state,n)
                available_numbers.remove(n)
                scor, _ = minimax(new_state, depth-1, available_numbers)
                if scor > best_scor:
                    best_scor = scor
                    best_value = n
    #human
    elif state["player"] == 1: 
        best_scor = float('inf') # minus infinit pt a gasi maxi
        best_value = None

        for n in available_numbers:
            new_state = copy.deepcopy(state)
            if validare_tranzitie(new_state,n):
                tranzitie(new_state,n)
                available_numbers.remove(n)
                scor, _ = minimax(new_state, depth-1, available_numbers)
                if scor < best_scor:
                    best_scor = scor
                    best_value = n

    return best_scor, best_value


def number_scrabble(state):
    available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while verificare_stare_finala(state) == 4:
        current_player = state["player"]
        print("Available Numbers:", available_numbers)
        print(f"Player {current_player}'s turn.")

        if current_player == 1: # human
            player_input = int(input("Choose a number: "))
            if not validare_tranzitie(state, player_input):
                print("Number already chosen or invalid number. Try again.")
                continue
            tranzitie(state,player_input)
            available_numbers.remove(player_input)
        
        else: # computer
            available_numbers_copy = copy.deepcopy(available_numbers)
            scor, player_input = minimax(state, 3, available_numbers_copy)
            if player_input == None:
                player_input = random.choice(available_numbers)
            print(f"Computer selects: {player_input}")
            tranzitie(state,player_input)
            available_numbers.remove(player_input)
        
    if verificare_stare_finala(state) == 1: 
        list_numbers = [state[f"n{i}"]["valoare"] for i in range(1, 10) if state[f"n{i}"]["owner"] == 1]
        for combo in combinations(list_numbers, 3):
            if sum(combo) == 15:
                combo_str = ' '.join(str(num) for num in combo)
                print("Human wins with combo: " + combo_str)
    elif verificare_stare_finala(state) == 2:
        list_numbers = [state[f"n{i}"]["valoare"] for i in range(1, 10) if state[f"n{i}"]["owner"] == 2]
        for combo in combinations(list_numbers, 3):
            if sum(combo) == 15:
                combo_str = ' '.join(str(num) for num in combo)
                print("Computer wins with combo: " + combo_str)
    elif verificare_stare_finala(state) == 3:
        print("It's a tie! Everyboby is a winner..")

number_scrabble(initializare(1))


# 1 3 5 9 = HUMAN
# 8 7 3 6 = COMPUTER
# 5 3 9 6 8 = TIE
