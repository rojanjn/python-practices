import random

# list of words
words = [
    "spoon", "fork", "knife", "plate", "pot", "refrigerator", "freezer", "food", "oven", "bowl", "peeler", "grater", "ladle", "stove", "microwave", "whisk", "spatula", "glass", "mug", "cabinet", "container", "sink", "dishwasher", "cup", "pantry"
]

# picking a random word
chosen_word = random.choice(words)
word_length = len(chosen_word)

display = ["_"]*word_length
lives = 6 #number of wrong guesses allowed

print()
print("\033[1m=-=-=-=- WELCOME TO HANGSMAN =-=-=-=-\033[0m")
print(" ".join(display))
print("\033[34mCATEGORY: Things you find in the kitchen. \033[0m")

# main game loop
while "_" in display and lives > 0:
    guess = input("\nGuess a letter: ").lower()
    
    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
                
    else:
        lives -= 1
        print(f"\n\033[31m    WRONG!\033[0m Lives left: {lives}")
        
    print(" ".join(display))
    
if "_" not in display:
    print("\n\033[32mYOU WON 🎉\033[0m Pretty smart eh?")
else:
    print(f"\n\033[1m\33[31mYOU LOST 💀\033[0m\033[0m The word was \033[4m'{chosen_word}'\033[0m.")