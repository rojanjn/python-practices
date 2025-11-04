import random
import time
import sys

# ASCII color escape code
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

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
        sys.stdout.write(f"\r{CYAN}Loading... [{bar * i}{' ' * (total - i)}] {percent}%{RESET}")
        sys.stdout.flush()
        time.sleep(duration / total)
    print("\n") 
        
# title screen
title = f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════╗
║                                                  ║
║      🎯  THE NUMBER GUESSING CHALLENGE  🎯      ║
║                                                  ║
╚══════════════════════════════════════════════════╝
{RESET}
"""
intro_lines = [
    f"{YELLOW}Three difficulty levels, one mission: guess the number.{RESET}",
    f"{YELLOW}The fewer chances you have, the sweeter the victory.{RESET}",
    "",
    f"{GREEN}Send me a screenshot of your best run, I'll add your name to the Game as the reigning champion 👑{RESET}",
    f"{MAGENTA}Guess it right on your first try, though… and you might just unlock a *secret reward*. 😏{RESET}",
]

print(title)
time.sleep(1)

slow_print(f"{CYAN}Initializing game environment...{RESET}")
loading_bar()

for line in intro_lines:
    slow_print(line, delay=0.04)
    time.sleep(0.5)
    
time.sleep(1)
slow_print(f"\n{WHITE}Pass {CYAN}Enter{WHITE} to begin your quest!{RESET}", delay=0.05)
input()
slow_print(f"{GREEN}Game starting in 3...{RESET}", 0.05)
time.sleep(0.5)
slow_print("2...", 0.5)
time.sleep(0.5)
slow_print("1...", 0.5)
time.sleep(0.5)
slow_print(f"{GREEN}{BOLD}GOOOO!!!{RESET}", 0.04)
time.sleep(1)

# getting user's name
name = input("\nWhat is your name gamer? ")
print(f"\nWelcome to the game {name}!")
# choosing difficulty
print(f"\n{name}, choose difficulty level: ")
print("1. Easy (Unlimited choices) \n2. Medium (Up to 25 choices)\n3. Hard (5 choices ONLY)")
difficulty = input("Choose 1, 2, or 3: ")

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