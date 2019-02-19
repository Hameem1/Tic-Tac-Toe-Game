from os import system

new_game = True
game_count = 0
player1_moves = [False for x in range(9)]
player2_moves = [False for x in range(9)]
winner = [False, False]
winning_set = [(1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 5, 3)]


def print_intro():
    print("\n'   Tic Tac Toe    '\n")
    print("Welcome to the game!\n")
    print("Player # 1 : X")
    print("Player # 2 : O")
    print("\nThis will be the position scheme of the board;")
    draw_board()


def draw_board(player1=[False for x in range(9)], player2=[False for x in range(9)]):
    # initialize an empty board
    board = ""
    print_text = []
    for i in range(9):
        if player1[i] == "X":
            print_text.append("X")
        elif player2[i] == "O":
            print_text.append("O")
        else:
            print_text.append(str(i+1))
    
    counter = 0
    for i in range(5):
        # switch between printing vertical and horizontal bars
        if i % 2 == 0:
            board += "|  " + print_text[counter] + "  " +\
                     "|  " + print_text[counter+1] + "  " +\
                     "|  " + print_text[counter+2] + "  " + "|  "
            counter += 3
        else:
            board += "  --- " * 3
        # don't forget to start a new line after each row using "\n"
        board += "\n"

    print("\n"+board)


def update_movelist(player, position):
    global player1_moves
    global player2_moves
    if player == 1:
        player1_moves[position-1] = "X"
    else:
        player2_moves[position-1] = "O"
    ret = win_checker()

    if ret == 1:
        return 1
    else:
        return 0


def win_checker():
    global winner
    ret = 0
    for win_set in winning_set:
        a, b, c = win_set
        if player1_moves[a - 1] == "X" and player1_moves[b - 1] == "X" and player1_moves[c - 1] == "X":
            winner[0] = True
            ret = announce_result()
        elif player2_moves[a - 1] == "O" and player2_moves[b - 1] == "O" and player2_moves[c - 1] == "O":
            winner[1] = True
            ret = announce_result()
        else:
            pass

    return ret
        

def announce_result():
    global new_game
    if winner[0]:
        print("Player 1 won the match. Congrats!")
    elif winner[1]:
        print("Player 2 won the match. Congrats!")
    elif winner[0] is False and winner[1] is False:
        print("The match was a DRAW!")
    else:
        print("<ERROR> Unknown result")
    
    decision = input("\n\nWould you like to start a new game? [y/n] :  ")
    if decision == "y":
        new_game = True
        return 1
    else:
        # print("Have a nice day.\nBye.\n")
        system("cls")
        exit()
        return 0


while new_game:
    new_game = False
    player1_moves = [False for x in range(9)]
    player2_moves = [False for x in range(9)]
    winner = [False, False]
    total_moves = 0
    game_count += 1
    if game_count == 1:
        print_intro()
    print(game_count)

    while total_moves < 9:
        draw_board(player1=player1_moves, player2=player2_moves)
        p1 = int(input("Player 1: Please enter the position to Mark 'X' :  "))
        ret1 = update_movelist(1, p1)
        if ret1 == 1:
            break
        total_moves += 1
        if total_moves >= 9:
            break        
        draw_board(player1=player1_moves, player2=player2_moves)
        p2 = int(input("Player 2: Please enter the position to Mark 'O':  "))
        ret2 = update_movelist(2, p2)
        
        if ret2 == 1:
            break
        total_moves += 1
    
    if total_moves == 9:
        announce_result()

# TODO: fix the problem where players can overwrite each others moves
#       fix the startup screen
