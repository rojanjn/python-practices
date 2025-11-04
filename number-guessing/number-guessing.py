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
RED = "\033[91m"

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(duration=2.5):
    bar = "█"
    total = 20
    for i in range(total + 1):
        percent = int((i / total) * 100)
        sys.stdout.write(f"\r{CYAN}Loading... [{bar * i}{' ' * (total - i)}] {percent}%{RESET}")
        sys.stdout.flush()
        time.sleep(duration / total)
    print("\n")

# title screen
def show_intro():
    title = f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════╗
║                                                  ║
║      🎯  THE NUMBER GUESSING CHALLENGE  🎯       ║
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
    slow_print(f"\n{WHITE}Press {CYAN}Enter{WHITE} to begin your quest!{RESET}", delay=0.05)
    input()
    slow_print(f"{GREEN}Game starting in 3...{RESET}", 0.05)
    slow_print("2...", 0.5)
    slow_print("1...", 0.5)
    slow_print(f"{GREEN}{BOLD}GOOOO!!!{RESET}", 0.04)
    time.sleep(1)

# GAME LOGIC
def play_game(name):
    secretNum = random.randint(1, 100)

    # Difficulty selection
    print(f"\n{name}, choose difficulty level: ")
    print("1. Easy (Unlimited attempts)\n2. Medium (Up to 25 attempts)\n3. Hard (Only 5 attempts!)")
    difficulty = input("Choose 1, 2, or 3: ")

    # Difficulty logic
    max_attempts = None
    if difficulty == "1":
        max_attempts = None
        slow_print(f"{GREEN}You chose easy. Take your time, {name}. No pressure :){RESET}")
    elif difficulty == "2":
        max_attempts = 25
        slow_print(f"{YELLOW}Medium Mode! Nice choice {name}. Balance of risk and glory ;){RESET}")
    elif difficulty == "3":
        max_attempts = 5
        slow_print(f"{MAGENTA}Oh my.. Hard mode?! Dang, {name}, you're savage. Let's see if you can beat the ruthless machine B){RESET}")
    else:
        slow_print(f"{CYAN}Hmm.. I'll assume you meant Easy, {name}. Well, LOL{RESET}")

    guess = None
    count = 0

    # Main guessing loop
    while True:
        if max_attempts is not None and count >= max_attempts:
            slow_print(f"{MAGENTA}Out of attempts, {name} :( \nThe number was {secretNum}.\nTry again. I KNOW you'll get it next time!{RESET}")
            break

        try:
            guess = int(input("\nGuess a number between 1 to 100: "))
        except ValueError:
            print(f"{RED}That's not a valid number, {name}! Try again!{RESET}")
            continue

        count += 1

        if guess < secretNum:
            print(f"{RED}Too low!{RESET} Attempt #{count}")
        elif guess > secretNum:
            print(f"{RED}Too high!{RESET} Attempt #{count}")
        else:
            slow_print(f"\n{GREEN}{BOLD}YOU WON 🎉{RESET} Honestly, you did better than ME!!!")
            slow_print(f"{CYAN}Incredible work, {name}! You guessed it in {count} attempts!{RESET}")

            if count == 1:
                slow_print(f"{MAGENTA}WAIT OH MY GOD!!! FIRST TRY?!!! You are an absolute GOAT! 🐐 LEGEND 🎉{RESET}")
            break

# MAIN LOOP (Play again system)
def main():
    show_intro()
    name = input("\nWhat is your name, gamer? ")
    slow_print(f"{GREEN}Welcome, {name}! Ready to test your instincts and luck? 🎯{RESET}", 0.04)

    user_tries = input(f"\n{YELLOW}Before we begin, how many tries do you *think* it'll take you to guess it? {RESET}")
    slow_print(f"{MAGENTA}Ooo {user_tries} tries? We'll see if your prediction holds up 😏🍀{RESET}")

    while True:
        play_game(name)
        choice = input(f"\n{CYAN}Wanna play again? (yes/no): {RESET}").lower()
        if choice not in ["yes", "y"]:
            print(f"{GREEN}\nThanks for playing, {name}! See you next time, champ. 👑{RESET}")
            break
        else:
            print(f"{YELLOW}\nRebooting your next challenge...{RESET}")
            loading_bar(1.5)

# Start the game
if __name__ == "__main__":
    main()
