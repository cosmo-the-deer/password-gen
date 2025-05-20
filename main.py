import random
import os
import time

#imports the list of charaters and puts them in a list
with open("characters.txt", "r") as file:
    characters = file.read().splitlines()

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("clr")
    else:
        raise Exception("Your system is not windows or uniux based system cannot clear")

#generates the password and returns it
def generate_password(length):
    if length == 0:
        length = 12
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def intro():
    print(r'''
 ____                                      _ 
|  _ \ __ _ ___ _____      _____  _ __ __| |
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
''')

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
        except ValueError:
            clear_screen()
            intro()
            print("ERROR Please enter a number")
            time.sleep(1)
            clear_screen()
            intro()

            continue
        clear_screen()
        intro()
        password = generate_password(length)
        print(f"generated password: {password}")
        print()

clear_screen()
intro()
main()