from itertools import permutations 
import random

def print_board(available_numbers):
    print("Available Numbers:", available_numbers)

def check_winner(selected_numbers):
    for i in range(len(selected_numbers)):
        for j in range(i + 1, len(selected_numbers)):
            for k in range(j + 1, len(selected_numbers)):
                if selected_numbers[i] + selected_numbers[j] + selected_numbers[k] == 15:
                    return True, [selected_numbers[i], selected_numbers[j], selected_numbers[k]]
    return False, []

def manhattan_distance(nums):
        target_sum = 15
        current_sum = sum(nums)
        return abs(target_sum - current_sum)

def computer_move(available_numbers, player_selections):
    best_move = None
    best_distance = float('inf')

    for num in available_numbers:
        computer_moves = player_selections['Computer'] + [num]
        distance = manhattan_distance(computer_moves)
        if distance < best_distance:
            best_distance = distance
            best_move = num
    return best_move

def number_scrabble():
    available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_selections = {'Human': [], 'Computer': []}
    current_player = 'Human'  # Human starts the game

    while available_numbers:
        print_board(available_numbers)
        print(f"Player {current_player}'s turn.")

        if current_player == 'Human':
            player_input = int(input("Choose a number: "))
            if player_input not in available_numbers:
                print("Number already chosen or invalid number. Try again.")
                continue
            player_selections['Human'].append(player_input)
        else:  # Computer's turn
            player_input = computer_move(available_numbers, player_selections)
            print(f"Computer selects: {player_input}")
            player_selections['Computer'].append(player_input)

        available_numbers.remove(player_input)

        has_won, winning_combination = check_winner(player_selections[current_player])
        if has_won:
            print(f"Player {current_player} wins with numbers: {player_selections[current_player]} ({'+'.join(map(str, winning_combination))})")
            break

        current_player = 'Computer' if current_player == 'Human' else 'Human'

    if not available_numbers and not has_won:
        print("It's a tie! No one reached 15 with any combination.")

number_scrabble()
