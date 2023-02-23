example = "1 2 3\n4 5 6\n7 8 9"
ttt_template = ["", "", "", "\n", "", "", "", "\n", "", "", ""]
print("Welcome to Tic-Tac-Toe!!!\n")
print(f"The grid numbers are below: \n\n{example}\n")
input("Press enter to start the game\n")
player_1_name = input("Player 1 name: ")
player_2_name = input("Player 2 name: ")


def game():
    player_1_choice = input(f"\n{player_1_name} it is your move! Where would you like to go: ")
    ttt_template[int(player_1_choice)] = "X"
    show_board()

    player_2_choice = input(f"\n{player_2_name} it is your move! Where would you like to go: ")
    ttt_template[int(player_2_choice)] = "O"
    show_board()

    check_if_won("X", player_1_name)
    check_if_won("O", player_2_name)

    if not check_if_won("X", player_1_name):
        game()


def check_if_won(letter, player_name):
    if ttt_template[0] and ttt_template[1] and ttt_template[2] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[3] and ttt_template[4] and ttt_template[5] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[6] and ttt_template[7] and ttt_template[8] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[0] and ttt_template[3] and ttt_template[6] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[1] and ttt_template[4] and ttt_template[7] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[2] and ttt_template[5] and ttt_template[8] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[0] and ttt_template[4] and ttt_template[8] == letter:
        print(f"{player_name} you won!!!")
        return True
    elif ttt_template[2] and ttt_template[4] and ttt_template[6] == letter:
        print(f"{player_name} you won!!!")
        return True


def show_board():
    for letter in ttt_template:
        print(letter[0:8])


game()
