from random import *
player = []
computer = []
skip = False
cskip = False
win = False
cchoice = ''
topcard = ''
deck = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',  '11', 'forcedraw', 'skip'] *2
colors = ['red', 'blue', 'green', 'yellow']
shuffle(deck)
def draw_card(drawer):
     random_card = deck.pop()
     random_color = choice(colors)
     random_card = f"{random_color} {random_card}"
     drawer.append(random_card)
print("Welcome to Color Numbers Game!")
random_card = deck.pop()
random_color = choice(colors)
topcard = f"{random_color} {random_card}"
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
    elif choice in player and (choice.split()[0] == topcard.split()[0] or choice.split()[1] == topcard.split()[1]):
        chosen_card = choice
        player.remove(chosen_card)
        topcard = chosen_card
        print(f"You played {chosen_card}. The new top card is {topcard}.")
        if chosen_card == 'yellow skip' or chosen_card == 'red skip' or chosen_card == 'blue skip' or chosen_card == 'green skip':
            skip = True
            print("You played a skip card! The computer will skip its turn.")
        if chosen_card == 'yellow forcedraw' or chosen_card == 'red forcedraw' or chosen_card == 'blue forcedraw' or chosen_card == 'green forcedraw':
            draw_card(computer)
            print("You played a forced draw card! The computer draws a card.")
    else:
        print("Invalid choice. Please try again.")
def ai(result):
    global cchoice
    valid_choices = [card for card in computer if card.split()[0] == topcard.split()[0] or card.split()[1] == topcard.split()[1]]
    if valid_choices:
        cchoice = choice(valid_choices)
        computer.remove(cchoice)
    else:
        draw_card(computer)
        cchoice = computer[-1]
def computerturn():
     global topcard, cskip, cchoice
     ai(cchoice)
     print(f"Computer plays {cchoice}.")
     topcard = cchoice
     print(f"The new top card is {topcard}.")
     if cchoice == 'yellow skip' or cchoice == 'red skip' or cchoice == 'blue skip' or cchoice == 'green skip':
            cskip = True
            print("Computer played a skip card! You skip your turn.")
     if cchoice == 'yellow forcedraw' or cchoice == 'red forcedraw' or cchoice == 'blue forcedraw' or cchoice == 'green forcedraw':
        draw_card(player)
        print("Computer played a forced draw card! You draw a card.")
def checkwin():
     global win
     if len(computer) == 1:
         print('Computer has 1 card left!')
     if len(player) == 0:
         print("You win!")
         win = True
     elif len(computer) == 0:
         print("Computer wins!")
         win = True
while win == False:
    if cskip == False:
        playerturn()
        checkwin()
    else:
        cskip = False
    if skip == False:
        computerturn()
        checkwin()
    else:
        skip = False