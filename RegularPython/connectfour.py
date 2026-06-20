def createboard():
    global board
    board = []
    for i in range(42):
        board.append(" ")
    return board
def printboard():
    global board
    print("0   1   2   3   4   5   6")
    print("{} | {} | {} | {} | {} | {} | {}".format(board[0], board[1], board[2], board[3], board[4], board[5], board[6]))
    print("-------------------------")
    print("{} | {} | {} | {} | {} | {} | {}".format(board[7], board[8], board[9], board[10], board[11], board[12], board[13]))
    print("-------------------------")
    print("{} | {} | {} | {} | {} | {} | {}".format(board[14], board[15], board[16], board[17], board[18], board[19], board[20]))
    print("-------------------------")
    print("{} | {} | {} | {} | {} | {} | {}".format(board[21], board[22], board[23], board[24], board[25], board[26], board[27]))
    print("-------------------------")
    print("{} | {} | {} | {} | {} | {} | {}".format(board[28], board[29], board[30], board[31], board[32], board[33], board[34]))
    print("-------------------------")
    print("{} | {} | {} | {} | {} | {} | {}".format(board[35], board[36], board[37], board[38], board[39], board[40], board[41]))
createboard()
def userinput(player):
    global board
    if player == 1:
        userin = input("Which column would you like to place your piece, player 1? (0-6, e.g. 1):")
    else:
        userin = input("Which column would you like to place your piece, player 2? (0-6, e.g. 1):")
    try:
        column = int(userin)
        if board[column] != " ":
            print("Sorry, but that column is full. Please pick another one.")
            userinput()
        else:
            if board[column+35] != " ":
                if player == 1:
                    board[column+35] = "X"
                else:
                    board[column+35] = "O"
            elif board[column+28] != " ":
                if player == 1:
                    board[column+28] = "X"
                else:
                    board[column+28] = "O"
            elif board[column+21] != " ":
                if player == 1:
                    board[column+21] = "X"
                else:
                    board[column+21] = "O"
            elif board[column+14] != " ":
                if player == 1:
                    board[column+14] = "X"
                else:
                    board[column+14] = "O"
            else:
                if player == 1:
                    board[column] = "X"
                else:
                    board[column] = "O"
    except:
        print("That is an incorrect input. Please try again just entering a single digit between 0 and 6.")
        userinput()
def main():
    pass