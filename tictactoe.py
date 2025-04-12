import random

win = False
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
possiblewins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
ppositions = []
cpositions = []

def drawboard():
    print(f"{board[0]}|{board[1]}|{board[2]}\n-----\n{board[3]}|{board[4]}|{board[5]}\n-----\n{board[6]}|{board[7]}|{board[8]}")

def askturn(turn):
    while True:
        turn = input('Who do you want to go first? (C, P): ').upper()
        if turn in ['C', 'P']:
            return turn
        else:
            print("Invalid input. Please enter 'C' for Computer or 'P' for Player.")

def askquestion():
    while True:
        chosensquare_str = input('Which square do you want to put an "O" in? (Numbers on board represent the squares.): ')
        if chosensquare_str.isdigit():
            chosensquare = int(chosensquare_str)
            if 1 <= chosensquare <= 9 and board[chosensquare - 1] not in ['X', 'O']:
                return chosensquare
            else:
                print("Invalid input. Please enter a number corresponding to an empty square on the board.")
        else:
            print("Invalid input. Please enter a number.")

def askcomp():
    while True:
        chosensquare = random.randint(1, 9)
        if board[chosensquare - 1] not in ['X', 'O']:
            return chosensquare

def replacepiece(chosensquare, turn):
    if turn == "C":
        board[chosensquare - 1] = 'X'
        cpositions.append(chosensquare)
    else:
        board[chosensquare - 1] = "O"
        ppositions.append(chosensquare)

def checkwin(positions, player):
    for win_combination in possiblewins:
        if all(pos in positions for pos in win_combination):
            print(f'{player} wins!!!!!!!')
            return True
    return False

def main():
    global win
    turn = askturn('')

    if turn == 'C':
        chosensquarecomp = askcomp()
        replacepiece(chosensquarecomp, "C")
        drawboard()
    else:
        drawboard()

    while not win:
        chosensquareplay = askquestion()
        replacepiece(chosensquareplay, 'P')
        drawboard()
        if checkwin(ppositions, "Player"):
            win = True
            break

        if all(item in ['X', 'O'] for item in board):
            print("It's a draw!")
            win = True
            break

        chosensquarecomp = askcomp()
        replacepiece(chosensquarecomp, 'C')
        drawboard()
        if checkwin(cpositions, 'Computer'):
            win = True
            break

        if all(item in ['X', 'O'] for item in board):
            print("It's a draw!")
            win = True
            break

    print('Thanks for playing!')

if __name__ == "__main__":
    main()