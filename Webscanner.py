import os, sys
import requests
from bs4 import BeautifulSoup


def logo():
        logo = '''
'\033[92m'
______     ______     ______     __        
/\  ___\   /\  __ \   /\  __ \   /\ \       
\ \ \____  \ \ \/\ \  \ \ \/\ \  \ \ \____  
 \ \_____\  \ \_____\  \ \_____\  \ \_____\ 
  \/_____/   \/_____/   \/_____/   \/_____/ 

 ______     ______   __  __     ______   ______  
/\  ___\   /\__  _\ /\ \/\ \   /\  ___\ /\  ___\ 
\ \___  \  \/_/\ \/ \ \ \_\ \  \ \  __\ \ \  __\ 
 \/\_____\    \ \_\  \ \_____\  \ \_\    \ \_\   
  \/_____/     \/_/   \/_____/   \/_/     \/_/   

                    ***We are Legion according to my discord friend***
'''
        return logo

OPTIONS = '''
1. Enter Domain Name to Search Users
2. Enter Specific Email Address
3. Exit
'''

def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)


def main():
    print(logo())
if __name__ == "__main__":
    main()
