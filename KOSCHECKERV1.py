import os
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_gold(text):
    print(Fore.YELLOW + text)

def print_ltblue(text):
    print(Fore.LIGHTBLUE_EX + text)

def print_red(text):
    print(Fore.RED + text)

def colorize_input(prompt):
    return input(Fore.YELLOW + prompt + Fore.RESET)

def search_kos(file_path, query_username):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                username = line.strip()
                if query_username == username:
                    print_red(f'{query_username} is KOS.')
                    return True
        return False
    except FileNotFoundError:
        print_gold(f'Error: File "{file_path}" not found.')
        return False

def search_guards(file_path, query_username):
    rank_mapping = {
        'P': 'Private',
        'SP': 'Specialist',
        'C': 'Corporal',
        'SG': 'Sergeant',
        'M': 'Master',
        'A': 'Admin',
        'HA': 'Head Admin'
    }

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                data = line.strip().split(' | ')
                username, rank_letter = data[0], data[1] if len(data) > 1 else None

                if query_username == username and rank_letter in rank_mapping:
                    rank = rank_mapping[rank_letter]
                    print_gold(f'{query_username} is a guard. RANK: {rank}.')
                    return True
        return False
    except FileNotFoundError:
        print_gold(f'Error: File "{file_path}" not found.')
        return False

if __name__ == "__main__":
    file_paths = ["KOS.txt", "GUARD.txt"]

    while True:
        print_ltblue("Made By IX (YehItzRue)")
        print_red("If person shows up as KOS and Guard check discord to see what they are and DM ixspectral to update.")
        search_query = colorize_input("Username: ")

        if search_kos(file_paths[0], search_query):
            print_red("!")
        else:
            if search_guards(file_paths[1], search_query):
                print_gold("+")
            else:
                print_gold(f'{search_query} Is not found.')

        input("")
        clear_screen()
