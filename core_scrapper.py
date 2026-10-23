#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Core Platform System Architecture: Core.Scrapper Extended Enterprise Pipeline
# Production Engineering Build: 3.2.4 [Release-Candidate Build]
# Lead Systems Engineer: Mr. Core
# Communication Node Location: t.me/real_mrcore

import os
import sys

# Dynamic standard system environment handler tracking
try:
    from backend.common.theme import COLOR_RED, COLOR_WHITE, RESET_ALL, clear_console_buffer
    from backend.interface.display import render_system_branding
    from backend.layers.module_html import execute_html_scraping_routine
    from backend.layers.module_css import execute_css_scraping_routine
except ImportError:
    # Append local system paths to prevent cross-module initialization errors
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from backend.common.theme import COLOR_RED, COLOR_WHITE, RESET_ALL, clear_console_buffer
    from backend.interface.display import render_system_branding
    from backend.layers.module_html import execute_html_scraping_routine
    from backend.layers.module_css import execute_css_scraping_routine

def start_framework_runtime():
    clear_console_buffer()
    while True:
        render_system_branding()
        print(f"{COLOR_WHITE}Select Automation Control Protocol Command Vector Option:")
        print(f"  {COLOR_RED}1.{COLOR_WHITE} HTML Structural Master Document Blueprint Scrapper")
        print(f"  {COLOR_RED}2.{COLOR_WHITE} CSS Layout Style Parameters Element Scrapper")
        print(f"  {COLOR_RED}3.{COLOR_RED} Terminate Core Framework Process Worker Instance (Exit)\n")
        
        choice = input(f"{COLOR_RED}Core.Scrapper > {RESET_ALL}").strip()

        if choice == "1":
            execute_html_scraping_routine()
            input(f"\n{COLOR_RED}[Pipeline State: Idle. Press Enter to synchronize Master Dashboard...]")
            clear_console_buffer()
        elif choice == "2":
            execute_css_scraping_routine()
            input(f"\n{COLOR_RED}[Pipeline State: Idle. Press Enter to synchronize Master Dashboard...]")
            clear_console_buffer()
        elif choice == "3":
            print(f"\n{COLOR_RED}[+]{COLOR_WHITE} Framework thread workers safely destroyed. Environment detached cleanly. Goodbye, Mr. Core!\n")
            sys.exit(0)
        else:
            print(f"\n{COLOR_RED}[-] Configuration Error: Selection parameter vector mapping must be 1, 2, or 3.")
            input(f"\n{COLOR_RED}[Pipeline State: Idle. Press Enter to re-align internal dashboard synchronization loops...]")
            clear_console_buffer()

if __name__ == "__main__":
    try:
        start_framework_runtime()
    except KeyboardInterrupt:
        print(f"\n\n{COLOR_RED}[-]{COLOR_WHITE} Force Shutdown Intercepted: Production runtime environment suspended by User Break.")
        sys.exit(0)
