#initialize thr required variables
import random
randomized_number = random.randint(1, 1000)
win = False
guess_count = 0
#initialize the required functions
def ask_user():
    user_guess = input("Guess a number between 1 and 1000:")
    return int(user_guess)
def main():
    global guess_count, win
    userinput = ask_user()
    if userinput == randomized_number:
        print("Congratulations! You guessed the correct number! The number was " + str(randomized_number)+ ". You solved it in " + str(guess_count) + " guesses!")
        win = True
    elif userinput < randomized_number:
        print("Your guess is lower than the correct number. Guess higher!")
    else:
        print("Your guess is higher than the correct number. Guess lower!")
    guess_count += 1
#main game loop: does not stop until the user wins
while not win:
    main()