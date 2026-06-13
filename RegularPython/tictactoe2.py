win = False
playerpieces = []
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
def userinput():
    global board
    user = input("Where do you want to place your piece? (row, column):")
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
            board[index] = "X"
            playerpieces.append(index)
    except:
        print("Invalid input. Please enter row and column separated by a comma. (for example, 0,1)")
        return userinput()
def checkforwin():
    global win
    winconditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if winconditions[i-1][0] in playerpieces and winconditions[i-1][1] in playerpieces and winconditions[i-1][2] in playerpieces:
            win = True
def main():
    while win == False:
        userinput()
        printboard()
        print(playerpieces)
        checkforwin()
    else:
        print("Win detected, player has won.")
createboard()
printboard()
main()
