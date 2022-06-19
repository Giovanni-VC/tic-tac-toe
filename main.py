# Import
import random
from random import random as rd


# TODO 1: Welcome, instructions and show the board

def welcome():

    print("Welcome to text-based version of the Tic Tac Toe game.")
    print("You play as X")

# TODO 2: Create variables for positions

avaliable_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

# TODO 3: Ask user for a position in the board

def ask_user_position():

    position_invalid = True
    global avaliable_positions

    while position_invalid:

        # TODO 4: Make the position chosen by the user no longer available

        user_position = str(input(f"Choose your position ({avaliable_positions}): "))
        if not (user_position in avaliable_positions):
            print("Opps you chose a wrong position!")
        else:
            position_invalid = False
            avaliable_positions.remove(user_position)
            return user_position

# TODO 5: Set the chosen by user position as 1

def set_user_position(user_position):

    global board

    if user_position == "1":
        board[0][0] = "X"
    elif user_position == "2":
        board[0][1] = "X"
    elif user_position == "3":
        board[0][2] = "X"
    elif user_position == "4":
        board[1][0] = "X"
    elif user_position == "5":
        board[1][1] = "X"
    elif user_position == "6":
        board[1][2] = "X"
    elif user_position == "7":
        board[2][0] = "X"
    elif user_position == "8":
        board[2][1] = "X"
    elif user_position == "9":
        board[2][2] = "X"


# TODO 6: Print the board with the user moves as "X"

def print_board():

    global board

    for line in board:

        for element in line:

            print(f"{element}", end=" ")

        print('')

# TODO 7: Check and show if anyone has won the game

def check_array(checker_list):

        if checker_list == ["X", "X", "X"]:
            return 'player'
        elif checker_list == ["O", "O", "O"]:
            return 'computer'
        else:
            return 'nobody'


def extract_board_lists():

    global board

    check_lists = []

    # Extract rows

    for i in range (0,3):

        row_list = []

        for j in range (0,3):

            row_list.append(board[i][j])

        check_lists.append(row_list)

    # Extract columns

    for j in range(0, 3):

        column_list = []

        for i in range(0, 3):
            column_list.append(board[i][j])

        check_lists.append(column_list)

    # Extract main diagonal

    main_diagonal = [board[0][0], board[1][1], board[2][2]]

    check_lists.append(main_diagonal)

    # Extract secondary diagonal

    secondary_diagonal = [board[0][2], board[1][1], board[2][0]]

    check_lists.append(secondary_diagonal)

    return check_lists

#Function to check who won the game

def who_won_the_game(table_arrays):

    for list in table_arrays:

        if check_array(list) == "computer":

            print("Computer wins!")
            return True

        elif check_array(list) == "player":

            print("Congrats you win!")
            return True


# TODO 8: Sort a position to computer

def computer_position():

    computer_position_invalid = True
    global avaliable_positions

    while computer_position_invalid:

        computer_position = str(random.randint(1, 9))
        if computer_position in avaliable_positions:

            computer_position_invalid = False
            avaliable_positions.remove(computer_position)
            return computer_position

# TODO 9: Set the position "chosen" by computer as 0

def set_computer_position(computer_chosen_position):

    global board


    if computer_chosen_position == "1":
        board[0][0] = "O"
    elif computer_chosen_position == "2":
        board[0][1] = "O"
    elif computer_chosen_position == "3":
        board[0][2] = "O"
    elif computer_chosen_position == "4":
        board[1][0] = "O"
    elif computer_chosen_position == "5":
        board[1][1] = "O"
    elif computer_chosen_position == "6":
        board[1][2] = "O"
    elif computer_chosen_position == "7":
        board[2][0] = "O"
    elif computer_chosen_position == "8":
        board[2][1] = "O"
    elif computer_chosen_position == "9":
        board[2][2] = "O"

# TODO 10: Print the board with the computer moves as "O"

# TODO 11: Check and show if anyone has won the game

# TODO 12: Ask if the user wants to play again

def main():

    run = True

    global avaliable_positions

    welcome()

    print_board()

    while True:

            set_user_position(ask_user_position())

            print_board()

            print("\n")


            if (who_won_the_game(extract_board_lists())) or (len(avaliable_positions) == 0):
                if avaliable_positions == 0:
                    print('Draw')

                break

            print("========================================")

            set_computer_position(computer_position())

            print_board()

            print("\n")

            if (who_won_the_game(extract_board_lists())) or (len(avaliable_positions) == 0):
                if avaliable_positions == 0:
                    print('Draw')
                break

main()

