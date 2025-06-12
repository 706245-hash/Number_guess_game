import random
from colorama import init, Fore, Back, Style

# Initialize colorama (automatically resets colours after each print)
init(autoreset=True)

def play_game():
    # Difficulty presets with colour-coded names
    DIFFICULTY = {
        '1': {'name': f'{Fore.GREEN}Beginner{Style.RESET_ALL}', 'range': (1, 50), 'attempts': 10},
        '2': {'name': f'{Fore.YELLOW}Intermediate{Style.RESET_ALL}', 'range': (1, 100), 'attempts': 7},
        '3': {'name': f'{Fore.RED}Expert{Style.RESET_ALL}', 'range': (1, 500), 'attempts': 5},
        '4': {'name': f'{Fore.CYAN}Custom{Style.RESET_ALL}', 'custom': True}
    }

    # Colourful title
    print(f"\n{Back.BLUE}{Fore.WHITE}=== NUMBER GUESSING GAME ==={Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Select Difficulty:{Style.RESET_ALL}")
    
    for key, value in DIFFICULTY.items():
        if not value.get('custom'):
            print(f"{Fore.CYAN}{key}.{Style.RESET_ALL} {value['name']} {Fore.WHITE}({value['range'][0]}-{value['range'][1]}){Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}{key}.{Style.RESET_ALL} {value['name']}")

    # Validate difficulty input
    while True:
        choice = input(f"{Fore.YELLOW}Enter choice (1-4): {Style.RESET_ALL}")
        if choice in DIFFICULTY:
            break
        print(f"{Fore.RED}Invalid input. Enter 1-4.{Style.RESET_ALL}")

    # Set game parameters
    if choice == '4':  # Custom mode
        while True:
            try:
                min_num = int(input(f"{Fore.YELLOW}Enter minimum number: {Style.RESET_ALL}"))
                max_num = int(input(f"{Fore.YELLOW}Enter maximum number: {Style.RESET_ALL}"))
                if max_num > min_num:
                    break
                print(f"{Fore.RED}Maximum must be greater than minimum.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Enter integers.{Style.RESET_ALL}")
        max_attempts = int(input(f"{Fore.YELLOW}Enter max attempts: {Style.RESET_ALL}"))
    else:
        min_num, max_num = DIFFICULTY[choice]['range']
        max_attempts = DIFFICULTY[choice]['attempts']

    random_int = random.randint(min_num, max_num)
    print(f"\n{Fore.BLUE}Difficulty:{Style.RESET_ALL} {DIFFICULTY[choice]['name']} | {Fore.BLUE}Range:{Style.RESET_ALL} {Fore.GREEN}{min_num}-{max_num}{Style.RESET_ALL} | {Fore.BLUE}Attempts:{Style.RESET_ALL} {Fore.RED}{max_attempts}{Style.RESET_ALL}")

    remaining = max_attempts
    won = False
    previous_diff = float('inf')

    while remaining > 0:
        print(f"\n{Fore.YELLOW}Attempts left:{Style.RESET_ALL} {Fore.RED if remaining <= 3 else Fore.YELLOW}{remaining}{Style.RESET_ALL}")
        try:
            guess = int(input(f"{Fore.CYAN}Guess: {Style.RESET_ALL}"))
            if guess < min_num or guess > max_num:
                print(f"{Fore.RED}Guess must be between {min_num} and {max_num}.{Style.RESET_ALL}")
                continue
        except ValueError:
            print(f"{Fore.RED}Enter a valid number.{Style.RESET_ALL}")
            continue

        if guess == random_int:
            print(f"\n{Back.GREEN}{Fore.WHITE}=== YOU WIN! ==={Style.RESET_ALL} 🎉")
            attempts_used = max_attempts - remaining + 1
            
            # Colourful win messages
            if attempts_used == 1:
                print(f"{Fore.MAGENTA}First try! {Fore.YELLOW}Legendary! {Fore.CYAN}🤯")
            elif attempts_used <= 3:
                print(f"{Fore.YELLOW}{attempts_used} tries! {Fore.GREEN}Impressive! {Fore.BLUE}😎")
            elif attempts_used <= max_attempts // 2:
                print(f"{Fore.GREEN}Good job! {Fore.YELLOW}👍")
            else:
                print(f"{Fore.CYAN}Phew! {Fore.MAGENTA}Close one! {Fore.RED}😅")
            won = True
            break
        else:
            # Warm/Cold hints with colour
            current_diff = abs(guess - random_int)
            if current_diff < previous_diff:
                print(f"{Fore.RED}Getting warmer! {Fore.YELLOW}🔥")
            elif current_diff > previous_diff:
                print(f"{Fore.BLUE}Getting colder! {Fore.CYAN}❄️")
            previous_diff = current_diff

            # High/Low feedback with colour
            if guess > random_int:
                print(f"{Fore.RED}Too high! {Fore.YELLOW}⬇️")
            else:
                print(f"{Fore.BLUE}Too low! {Fore.CYAN}⬆️")
            remaining -= 1

    # Endgame messages
    if not won:
        print(f"\n{Back.RED}{Fore.WHITE}=== GAME OVER ==={Style.RESET_ALL}")
        print(f"The number was {Fore.GREEN}{random_int}{Style.RESET_ALL}.")
    print(f"\n{Fore.MAGENTA}Thanks for playing! {Fore.YELLOW}👋{Style.RESET_ALL}")

# Main game loop
if __name__ == "__main__":
    while True:
        play_game()
        if input(f"\n{Fore.YELLOW}Play again? (y/n): {Style.RESET_ALL}").lower() != 'y':
            print(f"{Fore.MAGENTA}\nGoodbye! Come back soon! {Fore.CYAN}✨{Style.RESET_ALL}")
            break
