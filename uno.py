from random import *
player = []
computer = []
skip = False
cskip = False
win = False
topcard = ''
deck = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',  'wild', 'forcedraw', 'skip'] *2
shuffle(deck)
def draw_card(drawer):
     random_card = deck.pop()
     drawer.append(random_card)
print("Welcome to Numbers Game!")
topcard = deck.pop()
print(f"The top card is: {topcard}")
def initdecks():
     for i in range(7):
            draw_card(player)
            draw_card(computer)
initdecks()
def playerturn():
    global topcard, skip
    print('Your deck: \n', player)
    choice = input("Choose a card to play or type 'draw' to draw a card: ")
    if choice.lower() == 'draw':
        draw_card(player)
        print(f"You drew a card. Your deck is now: {player}")
    elif choice in player:
        chosen_card = choice
        player.remove(chosen_card)
        topcard = chosen_card
        print(f"You played {chosen_card}. The new top card is {topcard}.")
        if chosen_card == 'skip':
            skip = True
            print("You played a skip card! The computer will skip its turn.")
        if chosen_card == 'forcedraw':
            draw_card(computer)
            print("You played a forced draw card! The computer draws a card.")
    else:
        print("Invalid choice. Please try again.")
def computerturn():
     global topcard, cskip
     cchoice  = computer.pop()
     print(f"Computer plays {cchoice}.")
     topcard = cchoice
     print(f"The new top card is {topcard}.")
     if cchoice == 'skip':
            cskip = True
            print("Computer played a skip card! You skip your turn.")
     if cchoice == 'forcedraw':
        draw_card(player)
        print("Computer played a forced draw card! You draw a card.")
def checkwin():
     global win
     if len(player) == 0:
         print("You win!")
         win = True
     elif len(computer) == 0:
         print("Computer wins!")
         win = True
while win == False:
    if skip == False:
        playerturn()
        checkwin()
    else:
        skip = False
    if skip == False:
        try:
            computerturn()
            checkwin()
        except:
            print("Computer is annoying")
    else:
        skip = False