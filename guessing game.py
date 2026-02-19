print("welcome user to the guessing the game")
import random
beast = random.randint(1,600)
guess = int(input("Guess the number: "))
if guess == beast:
    print("Congratulations! You guessed the number correctly.")
else:
    print("try again LATER, the ans is ", beast)
