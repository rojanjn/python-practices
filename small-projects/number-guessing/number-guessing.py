import random

# computer picks a random number
secretNum = random.randint(1,100)

# intro
print("\n\033[1m----------- WELCOME TO THE NUMBER-GUESSING GAME -----------\033[0m")
print("\nIn this game, the computer will randomly choose a number between 1 to 100 and you have to guess the number. You have unlimited number of choices.")
print("\n----------- Let the game begin... -----------")

# get user's guesses
guess = None
count = 0

while guess != secretNum:
    count += 1

    guess = int(input("\nGuess a number between 1 to 100: "))
    
    if guess < secretNum:
        print(f"\033[31mToo low!\033[0m Attempt #{count}")
    elif guess > secretNum:
        print(f"\033[31mToo high!\033[0m Attempt #{count}")
    else:
        print("\n\033[32mYOU WON 🎉\033[0m Honestly, you did better than ME!!!")