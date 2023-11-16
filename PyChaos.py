import time
import os
from colorama import Fore, Style
import requests
from urllib import request
import colorama
import json
from requests import get, exceptions
import shutil
from argparse import ArgumentParser
import threading
import itertools
import socket
import geoip2.database
import nmap
def show_banner():
    print("""___  _   _    ____ _  _ ____ ____ ____
|__]  \_/  __ |    |__| |__| |  | [__
|      |      |___ |  | |  | |__| ___]
""")

def main():
    print_centered("COYOTI", Fore.WHITE)
    print_centered("CORP", Fore.RED)

    show_banner()
    load_progress_bar(100, require_internet=True)

    username = input_centered(f"{Fore.YELLOW}Por favor, escolha um nome de usuário:{Style.RESET_ALL} ")
    print(f"\n{Fore.YELLOW}Iniciando...{Style.RESET_ALL}")
    time.sleep(3)
    clear_screen()

    show_menu(username)

def print_centered(text, color):
    terminal_width = os.get_terminal_size().columns
    print(f"{color}{text.center(terminal_width)}{Style.RESET_ALL}")

def input_centered(prompt):
    terminal_width = os.get_terminal_size().columns
    return input(f"{prompt}".center(terminal_width))

def load_progress_bar(target_percentage, require_internet=False):
    current_percentage = 0
    while current_percentage <= target_percentage:
        if current_percentage == 15 and require_internet:
            if not is_internet_available():
                print("\nLIGUE O WI-FI E REINICIE A FERRAMENTA")
                exit()

        print(f"\rProgresso: {current_percentage}%", end="")
        time.sleep(0.1)

        if current_percentage == 37:
            time.sleep(0.5)
            current_percentage = 44
        elif current_percentage == 44:
            time.sleep(0.5)
            current_percentage = 46
        elif current_percentage == 46:
            time.sleep(2)
            current_percentage = 58
        elif current_percentage == 58:
            time.sleep(2)
            current_percentage = 61
        elif current_percentage == 61:
            time.sleep(2)
            current_percentage += 1
        elif current_percentage == 77:
            time.sleep(3)
            current_percentage = 80
        elif current_percentage == 80:
            time.sleep(2)
            current_percentage = 83
        elif current_percentage == 83:
            time.sleep(4)
            current_percentage = 86
        elif current_percentage == 86:
            time.sleep(2)
            current_percentage = 91
        elif current_percentage == 91:
            time.sleep(5)
            current_percentage = 93
        elif current_percentage == 93:
            time.sleep(2)
            current_percentage += 1
        elif current_percentage == 98:
            time.sleep(4)
            current_percentage = 100
            time.sleep(4)
        else:
            current_percentage += 1

    os.system('clear')
    print("\nProgresso completo!")
    time.sleep(1.9)


def is_internet_available():
    # Verificar a disponibilidade da internet (implementação simulada)
    return True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu(username):
    while True:
        clear_screen()
        print(f"{Fore.YELLOW}USER VIP: {username}")
        print(Fore.WHITE+"\nMenu:")
        print(f"{Fore.GREEN}1. IP-SCAN\n2. EMAILBOMB\n3. ENCURTADOR DE LINK\n4. SAIR{Style.RESET_ALL}")

        selected_option = input("\nEscolha uma opção: ")
        if selected_option == '1' or selected_option.upper() == 'IP-SCAN':
            exec(open("ipscan.py").read())
        elif selected_option == '2' or selected_option.upper() == 'EMAILBOMB':
            exec(open("emailbomb.py").read())
        elif selected_option == '3' or selected_option.upper() == 'ENCURTADOR DE LINK':
            exec(open("encurtador.py").read())
        elif selected_option == "4":
            print("Saindo...")
            time.sleep(2)
            clear_screen()
            return
        else:
            print("Item inválido, tente novamente.")
            time.sleep(2)

def execute_script(script_name):
    # Adicione a lógica real para executar o script desejado
    script_path = f"{script_name}.py"
    if os.path.exists(script_path):
        os.system(f'python {script_path}')
    else:
        print(f"Script {script_name} não encontrado.")

if __name__ == "__main__":
    main()