import random
import os

letters = []

def load_from_file():
    global letters
    with open("sym.txt", 'r') as file:
        letters = file.read().split()

def generateKey(length):
    key = ''
    for i in range(length):
        key = key + random.choice(letters)
    return key

def main():
    while True:
        print()
        print('type \"gen + length\" to generate a password or "clear" to clear the screen.')
        tput = input().replace('gen', '').lower()
        if tput == 'clear':
            if os.name == 'nt':
                os.system('clr')
            else:
                os.system('clear')
        else:
            tput = int(tput.strip())
            print()
            print(generateKey(tput))

load_from_file()
main()