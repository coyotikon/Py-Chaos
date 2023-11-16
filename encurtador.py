#code
#python
#url
#encurtador
'''
coded by:                            

AIKON  NEXUS  ψ

'''

import time
import pyshorteners
import os
from colorama import Fore,Back,Style
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
clearConsole()

print(Fore.LIGHTBLUE_EX+'''

N.E.         NEXUS EYE
 ## #                   ##                   ###########
####                  ##                  ###########
##    ##              ##                  ##
##      ##            ##                  ##
##       ##           ##                  ###########
##          ##        ##                  ##
##           ##       ##                  ##
##             ##     ##                  ###########
##               #####      ##       ###########
                                  
''')
url = input(Fore.LIGHTYELLOW_EX+"[@] coloque aqui o Link (url) ---> "+Fore.LIGHTGREEN_EX)

shrt = pyshorteners.Shortener()

nurl = shrt.tinyurl.short(url) 

print(Fore.LIGHTYELLOW_EX+"[@] aqui está seu novo Link  ---> " +Fore.LIGHTGREEN_EX+nurl)

time.sleep(4)
print(Fore.LIGHTMAGENTA_EX+'''
coded by:                            
●●●                  
●  ●                 
●   ●              
●    ●            
●AIKON●               
●      ●        
●       ●        
●        ●          
 ''' )
