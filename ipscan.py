#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil
from urllib import request
import colorama
import os
import json
import re

os.system("clear")

colorama.init()


def Header():
    print(colorama.Fore.RED+"""
\033[1;31m
$$$$$$\ $$$$$$$\   $$$$$$\                               
\_$$  _|$$  __$$\ $$  __$$\                              
  $$ |  $$ |  $$ |$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  
  $$ |  $$$$$$$  |\$$$$$$\  $$  _____|\____$$\ $$  __$$\ 
  $$ |  $$  ____/  \____$$\ $$ /      $$$$$$$ |$$ |  $$ |
  $$ |  $$ |      $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |
$$$$$$\ $$ |      \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |
\______|\__|       \______/  \_______|\_______|\__|  \__|
                                    \033[1;39mDeveloper by Eratonos\Agent.17\feltonhack\giglano \033[1;31m
""".center(shutil.get_terminal_size().columns))


Header()

while True:
    print(colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN + "[+] " + colorama.Fore.LIGHTRED_EX + "İP Adresini Daxil Edin ↓IP adress↓   Endereço IP ↓")
    ip = input(colorama.Style.RESET_ALL+"> ")

    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    p = re.compile(regex)

    if (re.search(p, ip)):
        url = 'https://ipapi.co/' + ip + '/json/'
        req = request.Request(url)
        response = request.urlopen(req)
        result = json.loads(response.read().decode("utf-8"))

        if len(result) == 5:
            print(colorama.Fore.RED+f"\n\033[1;3mError: {str(result['reason'])}\033[0m\n"+
                colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· IP · {colorama.Fore.LIGHTGREEN_EX+str(result['ip'])}\n"+
                colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Type · {colorama.Fore.LIGHTGREEN_EX+str(result['version'])}")

        else:
            print(colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· IP · {colorama.Fore.LIGHTGREEN_EX+str(result['ip'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Network · {colorama.Fore.LIGHTGREEN_EX+str(result['network'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Type · {colorama.Fore.LIGHTGREEN_EX+str(result['version'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Country · {colorama.Fore.LIGHTGREEN_EX+str(result['country_name'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Country Code · {colorama.Fore.LIGHTGREEN_EX+str(result['country'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Country Phone · {colorama.Fore.LIGHTGREEN_EX+str(result['country_calling_code'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Country Tld · {colorama.Fore.LIGHTGREEN_EX+str(result['country_tld'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Region · {colorama.Fore.LIGHTGREEN_EX+str(result['region'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· City · {colorama.Fore.LIGHTGREEN_EX+str(result['city'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Asn · {colorama.Fore.LIGHTGREEN_EX+str(result['asn'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Org · {colorama.Fore.LIGHTGREEN_EX+str(result['org'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Timezone · {colorama.Fore.LIGHTGREEN_EX+str(result['timezone'])} ({colorama.Fore.LIGHTGREEN_EX+str(result['utc_offset'])})\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Currency ·  {colorama.Fore.LIGHTGREEN_EX+str(result['currency_name'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Country Population · {colorama.Fore.LIGHTGREEN_EX+str(result['country_population'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Languages · {colorama.Fore.LIGHTGREEN_EX+str(result['languages'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Postal · {colorama.Fore.LIGHTGREEN_EX+str(result['postal'])}\n"+
                  colorama.Fore.LIGHTYELLOW_EX+f"\033[1;3m· Location · {colorama.Fore.LIGHTGREEN_EX+'https://google.com/maps/place/'+str(result['latitude'])},{str(result['longitude'])} ({str(result['latitude'])},{str(result['longitude'])})")
                  
        resp = input("Type 'exit' or 'sair' to leave, and if you don't want to exit, just press tab. |    Çıxmaq üçün 'exit' və ya 'sair' yazın, və çıxmaq istəmirsəniz, sadəcə tab düyməsini basın. |   Digite 'sair' ou 'exit' para sair, e caso não queira sair, basta pressionar a tecla tab:    ")
        if resp.lower() == 'sair' or resp.lower() == 'exit':
            exit()
    else:
        print(colorama.Fore.GREEN + "[-] " + colorama.Fore.RED + "The IP address is incorrect! |    İP ünvanı səhvdir! |    O endereço IP está incorreto!")