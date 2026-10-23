import os
from colorama import Fore, Style

# Strict Red & White Theme Global Matrix Configuration
COLOR_RED = Fore.RED + Style.BRIGHT
COLOR_WHITE = Fore.WHITE + Style.BRIGHT
RESET_ALL = Style.RESET_ALL

def clear_console_buffer():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
