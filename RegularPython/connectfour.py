player1pieces = []
player2pieces = []
player1win = False
player2win = False
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
            userinput(player)
        else:
            if board[column+35] == " ":
                if player == 1:
                    player1pieces.append(column+35)
                    board[column+35] = "X"
                else:
                    player2pieces.append(column+35)
                    board[column+35] = "O"
            elif board[column+28] == " ":
                if player == 1:
                    player1pieces.append(column+28)
                    board[column+28] = "X"
                else:
                    player2pieces.append(column+28)
                    board[column+28] = "O"
            elif board[column+21] == " ":
                if player == 1:
                    player1pieces.append(column+21)
                    board[column+21] = "X"
                else:
                    player2pieces.append(column+21)
                    board[column+21] = "O"
            elif board[column+14] == " ":
                if player == 1:
                    player1pieces.append(column+14)
                    board[column+14] = "X"
                else:
                    player2pieces.append(column+14)
                    board[column+14] = "O"
            elif board[column+7] == " ":
                if player == 1:
                    player1pieces.append(column+7)
                    board[column+7] = "X"
                else:
                    player2pieces.append(column+7)
                    board[column+7] = "O"
            else:
                if player == 1:
                    player1pieces.append(column)
                    board[column] = "X"
                else:
                    player2pieces.append(column)
                    board[column] = "O"
    except:
        print("That is an incorrect input. Please try again just entering a single digit between 0 and 6.")
        userinput(player)
def checkforwin():
    global player1win, player2win
    solutions = [
    [0,1,2,3], [1,2,3,4], [2,3,4,5], [3,4,5,6],
    [7,8,9,10], [8,9,10,11], [9,10,11,12], [10,11,12,13],
    [14,15,16,17], [15,16,17,18], [16,17,18,19], [17,18,19,20],
    [21,22,23,24], [22,23,24,25], [23,24,25,26], [24,25,26,27],
    [28,29,30,31], [29,30,31,32], [30,31,32,33], [31,32,33,34],
    [35,36,37,38], [36,37,38,39], [37,38,39,40], [38,39,40,41],
    [0,7,14,21], [7,14,21,28], [14,21,28,35],
    [1,8,15,22], [8,15,22,29], [15,22,29,36],
    [2,9,16,23], [9,16,23,30], [16,23,30,37],
    [3,10,17,24], [10,17,24,31], [17,24,31,38],
    [4,11,18,25], [11,18,25,32], [18,25,32,39],
    [5,12,19,26], [12,19,26,33], [19,26,33,40],
    [6,13,20,27], [13,20,27,34], [20,27,34,41],
    [0,8,16,24], [1,9,17,25], [2,10,18,26], [3,11,19,27],
    [7,15,23,31], [8,16,24,32], [9,17,25,33], [10,18,26,34],
    [14,22,30,38], [15,23,31,39], [16,24,32,40], [17,25,33,41],
    [21,15,9,3], [22,16,10,4], [23,17,11,5], [24,18,12,6],
    [28,22,16,10], [29,23,17,11], [30,24,18,12], [31,25,19,13],
    [35,29,23,17], [36,30,24,18], [37,31,25,19], [38,32,26,20]
    ]
    for i in range(69):
        if solutions[i-1][0] in player1pieces and solutions[i-1][1] in player1pieces and solutions[i-1][2] in player1pieces and solutions[i-1][3] in player1pieces:
            player1win = True
    for i in range(69):
        if solutions[i-1][0] in player2pieces and solutions[i-1][1] in player2pieces and solutions[i-1][2] in player2pieces and solutions[i-1][3] in player2pieces:
            player2win = True
def main():
    playernumber = 1
    while player1win == False and player2win == False:
        if playernumber == 1:
            userinput(1)
            playernumber = 2
        else:
            userinput(2)
            playernumber = 1
        printboard()
        print(player1pieces)
        print(player2pieces)
        checkforwin()
    else:
        if player1win == True:
            print("Win detected, player 1 has won.")
        else:
            print("Win detected, player 2 has won.")
createboard()
printboard()
main()