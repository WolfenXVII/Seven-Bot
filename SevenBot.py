from ast import While
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
def Reboot():
    cls()
    print('Rebooting')
    t5()
    cls()
    print('Rebooting.')
    t5()
    cls()
    print('Rebooting..')
    t5()
    cls()
    print('Rebooting...')
    cls()
def Glitch():
    cls()
    print("I'5l t$a6h yo# som8 >an*ers.")
    t5()
    cls()
    print("@'l^ 4e&c8 ?0u s!$e m*9ne666.")
    t5()
    cls()
    print("I'=l t!a\h !o~ s#m$ %^n>e7s.")
    t5()
    cls()
    print("0`ll $#9ch y!u #o5e ?|n+3rs.")
    t5()
    cls()
    print(Fore.RED + "Ar3 YOu sURE Y0U'rE Al0N3?" + Fore.WHITE)
    time.sleep(.1)
    cls()
    print("I'll teach you some manners.")
    t5()
    cls()

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
def insult():
    #Swear keywords dont work, only works if you type the exact phrase instead of the keywords
    if Reply in ["Fuck you" , "fuck you" , "Bitch" , "bitch" , "whore" , "Whore" , "Cunt" , "cunt" , "Asshole" , "asshole" , "Slut" , "slut" , "Piece of shit" , "piece of shit" , "Stupid" , "stupid" , "Idiot" , "idiot" , "Motherfucker" , "motherfucker" , "Fucker" , "fucker" ]:
        print(Fore.WHITE + "*Seven says 'Well... that wasn't very polite..." + Glitch()) #the part before Glitch doesn't show, also crash
        tc()
        print(Fore.RED + "*Seven devours your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        t()
        os.close
    else:
        print(Fore.GREEN + "something broke, fix it")
insult()
if Reply in ["Yes" , "yes"]:
    print("*Seven says 'Yes'")
    tc()
    print("*Mario Evaporates")
    tc()
    print("*Seven looks at you approvingly")
    tc()
    while True:
        Reply = input(Fore.WHITE + "*Seven says 'Do you want to play a game?': ")
        tc()
        insult()
        if Reply in ["no", "No"]:
            print(Fore.RED + "*Seven is insulted and shatters your soul, you abruptly cease existing.")
            tc()
            print(Fore.GREEN + "System: You have reached a bad ending please try again.")
            t()
            os.close()
        elif Reply in ["yes", "Yes"]:
            print("Let's play a friendly game of rock, paper, scissors.")
            rpsgame()
            tc()
            print(Fore.GREEN + "System: This section is still under development.")
        else:
            print(Fore.GREEN + "System: ERROR; please reply with 'Yes' or 'No'.")
            t()
            Reboot()
else:
    white()
    print(Fore.GREEN + "System: This section is still under development.")
white()
print(Fore.GREEN + "System: This section is still under development.")