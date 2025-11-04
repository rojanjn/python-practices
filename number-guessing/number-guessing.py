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
slow_print(f"{GREEN}Welcome, {name}! Ready to test your instincts and luck? 🎯{RESET}", 0.04)

user_tries = input(f"\n{YELLOW}Before we begin, tell me how many tries do you think it is gonna take you to guess: {RESET}")
slow_print(f"{MAGENTA}Ooo {user_tries} times? Wow! That's interesting... maybe it'll turn out like that, we shall see! 🍀{RESET}")
time.sleep(1)

# choosing difficulty
print(f"\n{name}, choose difficulty level: ")
print("1. Easy (Unlimited attempts) \n2. Medium (Up to 25 attempts)\n3. Hard (Only 5 attempts!)")

difficulty = input("Choose 1, 2, or 3: ")

# applying difficulty rules
if difficulty == "1":
    max_attempts = None
    slow_print(f"{GREEN}You chose easy. Take your time, {name}. No pressure :){RESET}")
elif difficulty == "2":
    slow_print(f"{YELLOW}Medium Mode! Nice choice {name}. Balance of risk and glory ;){RESET}")
elif difficulty == "3":
    slow_print(f"{MAGENTA}Oh my.. Hard mode?! Gang, {name}, you're savage. Let's see if you can beat the ruthless machine then B){RESET}")
else:
    max_attempts = None
    slow_print(f"{CYAN}Hmm.. I'll assume you meant Easy, {name}. Well, LOL{RESET}")
    
# GAME LOOP
# get user's guesses
guess = None
count = 0

while guess != secretNum:
    if max_attempts is not None and count >= max_attempts:
        slow_print(f"{MAGENTA}Out of attempts, {name} :( \nThe number was {secretNum}.\nTry again and I KNOW you'll get it this time!{RESET}")
        break
    
    count += 1
    try:
        guess = int(input("\nGuess a number between 1 to 100: "))
    except ValueError:
        print(f"\033[31mThat's not a valid number, {name}!\033[0m Try again!{RESET}")
        continue
    
    if guess < secretNum:
        print(f"\033[31mToo low!\033[0m Attempt #{count}")
    elif guess > secretNum:
        print(f"\033[31mToo high!\033[0m Attempt #{count}")
    else:
        slow_print(f"\n\033[32m{BOLD}YOU WON 🎉\033[0m Honestly, you did better than ME!!!")
        slow_print(f"{CYAN}Incredible work, {name}! You guessed it in {count} attempts!{RESET}")
        
        if count == 1:
            slow_print(f"WAIT OH MY GOD!!! FIRST TRY?!!! You are an absolute goat!{RESET}LEGEND 🎉")
            break