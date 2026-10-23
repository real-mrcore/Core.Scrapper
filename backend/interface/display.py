from backend.common.theme import COLOR_RED, COLOR_WHITE

def render_system_branding():
    # Raw string indicator added to bypass escape sequence flags
    ascii_layout = COLOR_RED + r"""
   ______                _____                                     
  / ____/___  ________  / ___/______________ _____  ____  ___  _____
 / /   / __ \/ ___/ _ \ \__ \/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /___/ /_/ / /  /  __/___/ / /__/ /  / /_/ / /_/ / /_/ /  __/ /    
\____/\____/_/   \___//____/\___/_/   \__,_/ .___/ .___/\___/_/     
                                          /_/   /_/                 
    """
    print(ascii_layout)
    print(f"{COLOR_RED} =" * 36)
    print(f"{COLOR_WHITE}  [+] System Architecture : {COLOR_RED}CORE{COLOR_WHITE}●{COLOR_RED}SCRAPPER{COLOR_WHITE} Extended Infrastructure Engine")
    print(f"{COLOR_WHITE}  [+] Engine Release Flag : {COLOR_WHITE}Version 3.2.4 [{COLOR_RED}Stable Production Build{COLOR_WHITE}]")
    print(f"{COLOR_WHITE}  [+] Systems Architect   : {COLOR_RED}Mr. Core")
    print(f"{COLOR_WHITE}  [+] Secure Comms Channel: {COLOR_RED}t.me/real_mrcore")
    print(f"{COLOR_RED} =" * 36 + "\n")
