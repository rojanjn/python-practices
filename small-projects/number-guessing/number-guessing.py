import random
import time
import sys
from colorama import Fore, Style, init
init(autoreset=True)

# computer picks a random number
secretNum = random.randint(1,100)

# intro
def slow_print(text, delay=0.05):
    # Print text slowly for a typewriter effect.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(duration=2.5):
    # simulate a loading bar animation
    bar = "█"
    total = 20
    
    for i in range(total + 1):
        percent = int((i/total) * 100)
        sys.stdout.write(f"\r{Fore.CYAN}Loading... [{bar * i}{' ' * (total - i)}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / total)
    print("\n") 
        
# title screen
title = f"""
{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════════════════╗
║                                                  ║
║      🎯  THE NUMBER GUESSING CHALLENGE  🎯      ║
║                                                  ║
╚══════════════════════════════════════════════════╝
"""
intro_lines = [
    f"{Fore.YELLOW}Three difficulty levels, one mission: guess the number.",
    f"{Fore.YELLOW}The fewer chances you have, the sweeter the victory.",
    "",
    f"{Fore.GREEN}Send me a screenshot of your best run, I'll add your name to the Game as the reigning champion 👑",
    f"{Fore.MAGENTA}Guess it right on your first try, though… and you might just unlock a *secret reward*. 😏",
]

print(title)
time.sleep(1)

slow_print(f"{Fore.CYAN}Initializing game environment...")
loading_bar()

for line in intro_lines:
    slow_print(line, delay=0.04)
    time.sleep(0.5)
    
time.sleep(1)
slow_print(f"\n{Fore.LIGHTWHITE_EX}Pass {Fore.CYAN}Enter{Fore.LIGHTWHITE_EX} to begin your quest!", delay=0.05)
input()
slow_print(f"{Fore.GREEN}Game starting in 3...", 0.05)
time.sleep(0.5)
slow_print("2...", 0.5)
time.sleep(0.5)
slow_print("1...", 0.5)
time.sleep(0.5)
slow_print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}GOOOO!!!", 0.04)
time.sleep(1)


# print("\n\033[1m----------- WELCOME TO THE NUMBER-GUESSING GAME -----------\033[0m")
# print("""
# Three difficulty levels, one mission: guess the number.
# The fewer chances you have, the sweeter the victory.\n
# Send me a screenshot of your best run — I'll add your name to the README as the reigning champion 👑\nGuess it right on your first try, though… and you might just unlock a *secret reward*. ;)
# """)
# print("----------- Let the game begin... -----------")

# getting user's name
name = input("\nWhat is your name gamer? ")

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