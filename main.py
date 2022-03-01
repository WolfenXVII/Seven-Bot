import keyboard
import time
from colorama import Fore, Back, Style
import os
import webbrowser

def t5():
    time.sleep(.5)
def t():
    time.sleep(5)
def cls():
    os.system('cls||clear')
def enter():
    print("")
def white():
    print(Fore.WHITE)
def tc():
    time.sleep(5)
    os.system('cls||clear')

cls()
print(Fore.WHITE + "Hey, im Seven.... and just to make sure were on the right page; I'm not seven years old; Seven is my name.")
tc()
Username = input("Whats your name?: ")
cls()
Moodle = input("Hi! " + Username + " How was your day today?: ")
t()
webbrowser.open("https://youtube.com/clip/Ugkx2dFTgPpjOraDAjRbe09JFApXp0VJuJbv")
cls()
print(Fore.RED + "*Seven breakdances on your dead corpse")
white()
time.sleep(20)
cls()
life = input("How was your life? Because its over now: ")
tc()
print(Fore.RED + "I am here to claim your soul")
white()
tc()
print("*Mario from the hit game; Mario, breaks down the door.")
time.sleep(3)
cls()
print("*Mario Says No")
time.sleep(3)
cls()
print("*Seven Says Yes")
time.sleep(3)
cls()
print("*Mario Says Yes")
time.sleep(3)
cls()
print("*Seven Says No")
time.sleep(3)
cls()
print("*They both look at you...")
time.sleep(3)
cls()
Reply = input("*Seven Says 'What do you think, traveling soul?': ")
tc()
if Reply in ["Yes" , "yes"]:
    print("*Seven says Yes")
    tc()
    print("*Mario Evaporates.")
    tc()
    print("*Seven looks at you approvingly.")
    tc()
    reply2 = input("*Seven Says 'Do you want to play a game?: ")
    if reply2 in ["no", "No"]:
        print(Fore.RED + "*Seven shatters your soul and you truly cease existing.")
        tc()
        print(Fore.GREEN + "System: You have reached the bad ending please try again.")
        t()
    else:
        print(Fore.GREEN + "System: This section is still under development.")
else:
    print(Fore.GREEN + "System: This section is still under development.")