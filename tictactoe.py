import random
win = False
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
possiblewins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[7,5,3]]
ppositions = []
cpositions = []
def drawboard():
    print(board[0]+'|'+board[1]+'|'+board[2]+/nboard[3]+'|'+board[4]+'|'+board[5]+/nboard[6]+"|"+board[7]+'|'+board[8])
def askturn(turn):
    turn = input('Who do you want to go first? (C, P)')
    return turn
def askquestion(chosensquare):
    chosensquare = input('Which square do you want to put an "O" in? (Numbers on board represent the squares.)')
    if int(chosensquare) in board:
        return chosensquare
    else:
        askquestion(chosensquare)
def askcomnp(chosensquare):
    yay = False
    while yay == False:
        chosensquare = random.randint(len(board))
        if chosensquare != 'X' or chosensquare != "O":
            yay = True
def replacepiece(chosensquare, turn):
    if turn == "c":
        board[int(chosensquare)-1] = 'X'
        cpositions.append(chosensquare)
    else:
        board[int(chosensquare)-1] = "O"
        ppositions.append(chosensquare)
def checkwin(list, player):
    index = 7
    for i in range(8):
        for possiblewins[index] in list:
            print(player+' wins!!!!!!!')
            win = True
def main():
    global win
    turn = ''
    chosensquareplay = ''
    chosensquarecomp = ''
    if askturn(turn) == 'C':
        askcomnp(chosensquarecomp)
        replacepiece(chosensquarecomp, "c")
        drawboard()
    else:
        drawboard()
    while win != True:
        askquestion(chosensquareplay)
        replacepiece(chosensquareplay, 'p')
        checkwin(ppositions, "Player")
        drawboard()
        askcomnp(chosensquarecomp)
        replacepiece(chosensquarecomp, 'c')
        checkwin(cpositions, 'Computer')
        printboard()
    print('Thanks for playing!')
