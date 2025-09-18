import random

# list of words
categories = {
    "things you find in the kitchen": [
        "spoon", "fork", "knife", "plate", "pot", "refrigerator", "freezer", "food", "oven", "bowl", "peeler", "grater", "ladle", "stove", "microwave", "whisk", "spatula", "glass", "mug", "cabinet", "container", "sink", "dishwasher", "cup", "pantry"
        ],
    "movie names": [
        "interstellar", "twilight", "harrypotter", "matrix", "inception", "titanic", "gladiator", "annabelle", "clueless", "parasite", "superman", "batman", "psychosynthesis", "separation", "midsommer", "cobacabana"
        ],
    "one-word celebrity names": [
        "oprah", "adele", "rihanna", "eminem", "madonna", "usher", "beyonce", "shakira", "sting", "queen", "sia", "kesha", "sza", "ronaldo", "messi", "obama", "avicii", "cardib", "mitski", "zendaya", "bangchan", "nayeon"
        ],
    "countries": [
        "canada", "america", "japan", "oman", "persia", "ireland", "southkorea", "australia", "finland", "rwanda", "hungary", "argentina", "morocco", "kazakhstan", "azerbaijan"
        ]
}

# ascii art
stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===
    """,
]

# picking a random word
chosen_word = random.choice(k_words)
word_length = len(chosen_word)

display = ["_"] * word_length
lives = 6 #number of wrong guesses allowed

print()
print("\033[1m=-=-=-=- WELCOME TO HANGSMAN =-=-=-=-\033[0m")
print("\nChoose a category please (1. things you might find in the kitchen, 2. ) ")
print(" ".join(display))
print("\033[34mCATEGORY: Things you find in the kitchen. \033[0m")

# main game loop
while "_" in display and lives > 0:
    print(stages[min(6 - lives, 6)])
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