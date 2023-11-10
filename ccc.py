import copy

#1

# reprezentam o stare ca o lista ce contine:
#    - o variabila "player" = {1,2}:
#         * 1 - este randul primului jucator
#         * 2 - este randul celui de-al doilea jucator (calculatorul)
#    - 9 dictionare (m_1 -> m_9). Fiecare dictionar va contine:
#         * "owner" = {0,1,2}. Daca este detinuta de jucatorul 1,2. Sau 0 daca nu este detinuta de nimeni.
#         * "value" = valoarea pusa de respectivul jucator.    

def initialize(first_player):
    if first_player not in {1, 2}:
        raise ValueError("Valoarea 'first_player' trebuie să fie 1 sau 2.")

    state = {
        "player": first_player,
        "m_1": {"owner": 0, "value": 0},
        "m_2": {"owner": 0, "value": 0},
        "m_3": {"owner": 0, "value": 0},
        "m_4": {"owner": 0, "value": 0},
        "m_5": {"owner": 0, "value": 0},
        "m_6": {"owner": 0, "value": 0},
        "m_7": {"owner": 0, "value": 0},
        "m_8": {"owner": 0, "value": 0},
        "m_9": {"owner": 0, "value": 0}
    }
    
    return state

def final_state(state):
    def check_winner(player):
        winning_combinations = [
            (1, 5, 9), (1, 6, 8), 
            (2, 4, 9), (2, 6, 7), 
            (3, 4, 8), (3, 5, 7), 
            (4, 5, 6)
        ]


        for combination in winning_combinations:
            find = 0
            for i in range(1, 10):
                if state[f"m_{i}"]["owner"] == player and int(state[f"m_{i}"]["value"]) in combination:
                    find = find + 1
            
            if find == 3:
                return True

        return False

    first_player_won = check_winner(1)
    second_player_won = check_winner(2)
    if first_player_won:
        return 1 # primul jucator a castigat
    elif second_player_won:
        return 2 # al doilea jucator a castigat
    elif all(state[f"m_{i}"]["owner"] != 0 for i in range(1, 10)):
        return 3 # remiza: nu mai pot fi alese numere si nu exista niciun castigator
    else:
        return 4 # jocul nu a ajuns la final
#2

def validate_value(value, state):
    for i in range(1, 10):
        if int(state[f"m_{i}"]["value"]) == value:
            return False

    return True

def assign_value(value, state):
    for i in range(1, 10):
        if state[f"m_{i}"]["owner"] == 0:
            state[f"m_{i}"]["value"] = value
            state[f"m_{i}"]["owner"] = state["player"]
            state["player"] = 3 - state["player"]  # Schimbă jucătorul curent.

            return True  

    return False

#3

def heuristic_score(state):
    current_player = state["player"]
    opponent = 3 - current_player
    
    opponent_score = 0

    opponent_values = set()
    current_player_values = set()
    winning_combinations = [
        (1, 5, 9), (1, 6, 8),
        (2, 4, 9), (2, 6, 7),
        (3, 4, 8), (3, 5, 7),
        (4, 5, 6), (2, 5, 8)
    ]

    for i in range(1, 10):
        if state[f"m_{i}"]["owner"] == opponent:
            opponent_values.add(state[f"m_{i}"]["value"])
        elif state[f"m_{i}"]["owner"] == current_player:
            current_player_values.add(state[f"m_{i}"]["value"])

    for combination in winning_combinations:

        found_in_opponent_player = False
        found_in_current_player = False
        for i in range(3):
            if combination[i] in opponent_values:
                found_in_opponent_player = True
            elif combination[i] in current_player_values:
                found_in_current_player = True

        if (found_in_opponent_player == False and found_in_current_player == True):  # or (found_in_opponent_player == False and found_in_current_player == False):
            opponent_score = opponent_score + 1
    
    return opponent_score

#4

def minimax(depth, state):
    current_player = state["player"]
    next_player = 3 - state["player"]

    if final_state(state) == True or depth == 0:
        return heuristic_score(state), None  # Returnăm și None pentru valoarea optimă
    if current_player == 2:  # Este calculatorul
        best_score = float('inf')  # Inițializăm cu infinit (pentru a găsi minimul)
        best_value = None

        available_values = set(range(1,10))

        for i in range(1, 10):
            if state[f"m_{i}"]["owner"] != 0:
                value_to_remove = state[f"m_{i}"]["value"]
                # print(f"Before discard: {available_values}")
                available_values.discard(int(value_to_remove))
                # print(f"After discard {value_to_remove}: {available_values}")
                # print(f"stergem {value_to_remove}")

        # print(f"Final available values: {available_values}")
        for value in available_values:
            new_state = copy.deepcopy(state)
            if validate_value(value, new_state):
                assign_value(value, new_state)
                score, _ = minimax(depth-1, new_state)

                if score < best_score:
                    best_score = score
                    best_value = value
        # print(f"best score: {best_score} si best value: {best_value}")
        return best_score, best_value

    elif current_player == 1:
        best_score = float('-inf')  # Inițializăm cu minus infinit (pentru a găsi maximul)
        best_value = None

        available_values = set(range(1,10))

        for i in range(1, 10):
            if state[f"m_{i}"]["owner"] != 0:
                value_to_remove = state[f"m_{i}"]["value"]
                # print(f"Before discard: {available_values}")
                available_values.discard(int(value_to_remove))
                # print(f"After discard {value_to_remove}: {available_values}")
                # print(f"stergem {value_to_remove}")

        # print(f"Final available values: {available_values}")
        for value in available_values:
            new_state = copy.deepcopy(state)
            if validate_value(value, new_state):
                assign_value(value, new_state)
                score, _ = minimax(depth-1, new_state)

                if score > best_score:
                    best_score = score
                    best_value = value

        return best_score, best_value



def game(state):
    response = final_state(state)

    while response == 4: # nu s-a ajuns la o stare finala
        current_player = state["player"]

        player_values = set()
        ai_values = set()

        for i in range(1, 10):
            if state[f"m_{i}"]["owner"] == 1:
                player_values.add(state[f"m_{i}"]["value"])
            elif state[f"m_{i}"]["owner"] == 2:
                ai_values.add(state[f"m_{i}"]["value"])
        
        if player_values != set():
            print("\nPlayer's choises: ", player_values)
        else:
            print("\nPlayer's choises: -")

        if ai_values != set():
            print("AI's choises: ", ai_values)
        else:
            print("AI's choises:  -")

        if current_player == 1: # jucatorul uman
            while True:
                print("\nIntroduceti o valoare:")

                user_input = input()
                try:
                    value = int(user_input) 
                    # print("Ati introdus valoarea:", value)
                except ValueError:
                    print("Valoarea introdusă nu este un număr valid.")

                if validate_value(value, state) == True and value > 0 and value < 10:
                    print(validate_value(value, state))
                    break
                else:
                    print("Valoarea introdusa nu este disponibila. Incercati din nou!")
            
            assign_value(value, state)
            response = final_state(state)

        else: # jucator AIz
            score, best_value = minimax(3, state)
            assign_value(best_value, state)
            print("\nAI-ul a ales valoarea ", best_value)
            response = final_state(state)

    if response == 1:
        print("Ai castigat!")
    elif response == 2:
        print("Ai pierdut! IA-ul este mai destept decat tine!")
    elif response == 3:
        print("Remiza! Incearca un alt joc!")
            


##################################################3

initial_state = initialize(1)

game(initial_state)

# print(heuristic_score(state))

# for key, value in initial_state.items():
#         if key == "player":
#             print(f"{key}: {value}")
#         else:
#             print(f"{key}:")
#             for attribute, attribute_value in value.items():
#                 print(f"  {attribute}: {attribute_value}")
