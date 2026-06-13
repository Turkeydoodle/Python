player1win = False
player2win = False
playerpieces1 = []
playerpieces2 = []
def createboard():
    global board
    board = []
    for i in range(9):
        board.append(" ")
    return board
def printboard():
    print(" 0   1   2") 
    print("0 {} | {} | {}".format(board[0], board[1], board[2]))
    print("-----------")
    print("1 {} | {} | {}".format(board[3], board[4], board[5]))
    print("-----------")
    print("2 {} | {} | {}".format(board[6], board[7], board[8]))
def userinput(player):
    global board
    if player == 1:
        user = input("Where do you want to place your piece, player 1? (row, column):")
    else:
        user = input("Where do you want to place your piece, player 2? (row, column):")
    try:
        row, column = user.split(",")
        row = int(row)
        column = int(column)
        index = row*3+column
        if row < 0 or row > 2 or column < 0 or column > 2:
            print("Sorry, please input a value between 0 and 2 for row and columns.")
            userinput()
        elif board[index] != " ":
            print("Sorry, but your selected square is already taken.")
            userinput()
        else:
            if player == 1:
                board[index] = "X"
                playerpieces1.append(index)
            else:
                board[index] = "O"
                playerpieces2.append(index)
    except:
        print("Invalid input. Please enter row and column separated by a comma. (for example, 0,1)")
        return userinput()
def checkforwin():
    global player1win, player2win
    winconditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if winconditions[i-1][0] in playerpieces1 and winconditions[i-1][1] in playerpieces1 and winconditions[i-1][2] in playerpieces1:
            player1win = True
    for i in range(8):
        if winconditions[i-1][0] in playerpieces2 and winconditions[i-1][1] in playerpieces2 and winconditions[i-1][2] in playerpieces2:
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
        print("Player 1 pieces: "+str(playerpieces1))
        print("Player 2 pieces: "+str(playerpieces2))
        checkforwin()
    else:
        if player1win == True:
            print("Win detected, player 1 has won.")
        else:
            print("Win detected, player 2 has won.")
createboard()
printboard()
main()
