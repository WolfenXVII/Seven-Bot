import random
import keyboard
import time
from colorama import Fore, Back, Style
import os
import webbrowser
rpsv = 0
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
def rpsgame():
    tc()
    rps = ["Rock", "Paper", "Scissors"]
    rrps = random.choice(rps)
    rpsa = input(Fore.GREEN + "System: Type 'Rock', 'Paper' or 'Scissors': ")
    white()
    tc()
    if rpsa == rrps:
        print("*Seven chooses " + rrps)
        tc()
        print("We tied? That's no fun, let's go again.")
        rpsgame()
    elif rpsa == "Rock" and rrps == "Paper":
        print("*Seven chooses " + rrps)
        tc()
        print("*Seven pull out a glock and says, 'Sorry kid, I only play high stakes.'")
        tc()
        print(Fore.RED + "*Seven shoots you with the glock, shattering your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        tc()
        exit()
    elif rpsa == "Rock" and rrps == "Scissors":
        print("*Seven chooses " + rrps)
        tc()
        print("Hmmm, you actually won... I guess I'll be nice and give you your body back.")
        tc()
        print(Fore.BLUE + "*Seven ressurects your body and places your soul back where it belongs.")
    elif rpsa == "Scissors" and rrps == "Paper":
        print("*Seven chooses " + rrps)
        tc()
        print("Hmmm, you actually won... I guess I'll be nice and give you your body back.")
        tc()
        print(Fore.BLUE + "*Seven ressurects your body and places your soul back where it belongs.")
    elif rpsa == "Scissors" and rrps == "Rock":
        print("*Seven chooses " + rrps)
        tc()
        print("*Seven pull out a glock and says, 'Sorry kid, I only play high stakes.'")
        tc()
        print(Fore.RED + "*Seven shoots you with the glock, shattering your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        tc()
        exit()
    elif rpsa == "Paper" and rrps == "Rock":
        print("*Seven chooses " + rrps)
        tc()
        print("Hmmm, you actually won... I guess I'll be nice and give you your body back.")
        tc()
        print(Fore.BLUE + "*Seven ressurects your body and places your soul back where it belongs.")
    elif rpsa == "Paper" and rrps == "Scissors":
        print("*Seven chooses " + rrps)
        tc()
        print("*Seven pull out a glock and says, 'Sorry kid, I only play high stakes.'")
        tc()
        print(Fore.RED + "*Seven shoots you with the glock, shattering your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        tc()
        exit()
    else:
        rpsgame()
cls()
print(Fore.WHITE + "Hey, I'm Seven... just to make sure we are on the right page; I'm not seven years old; Seven is my name.")
tc()
Username = input("What is your name?: ")
cls()
Moodle = input("Hi, " + Username + " How was your day today?: ")
t()
webbrowser.open("https://youtube.com/clip/Ugkx2dFTgPpjOraDAjRbe09JFApXp0VJuJbv")
cls()
print(Fore.RED + "*Seven breakdances on your dead corpse")
white()
time.sleep(20)
cls()
life = input("How was your life? Because it is over now: ")
tc()
print(Fore.RED + "I am here to claim your soul")
white()
tc()
print("*Mario from the hit game; Mario, breaks down the door.")
time.sleep(3)
cls()
print("*Mario says 'No'")
time.sleep(3)
cls()
print("*Seven says 'Yes'")
time.sleep(3)
cls()
print("*Mario says 'Yes'")
time.sleep(3)
cls()
print("*Seven says 'No'")
time.sleep(3)
cls()
print("*They both look at you...")
time.sleep(3)
cls()
Reply = input("*Seven says 'What do you think, kid?': ")
tc()
while True:
    if Reply in ["Yes" , "yes"]:
        print("*Seven says 'Yes'")
        tc()
        print("*Mario Evaporates")
        tc()
        print("*Seven looks at you approvingly")
        tc()
        reply2 = input("*Seven says 'Do you want to play a game?': ")
        tc()
        if reply2 in ["no", "No"]:
            print(Fore.RED + "*Seven is insulted and shatters your soul, you abruptly cease existing.")
            tc()
            print(Fore.GREEN + "System: You have reached a bad ending please try again.")
            t()
        elif reply2 in ["yes", "Yes"]:
            print("Let's play a friendly game of rock, paper, scissors.")
            rpsgame()
    else:
        white()
        print(Fore.GREEN + "System: Please answer with 'Yes' or 'No'.")
    white()
    print(Fore.GREEN + "System: This section is still under development.")