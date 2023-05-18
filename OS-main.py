import time
import sys
from calculator import *
from notepadc import *
from clock import *
from weather import *

areWeDone = False

print("\n\n\n\n\n\n\nWelcome to Avneet's mini operating system!\n")

def osMenu():
    print("     ________________________")
    print("    | ☆                    ☆ |")
    print("    | ☆    1) Calculator   ☆ |")
    print("    | ☆                    ☆ |")
    print("    | ☆     2) Notepad     ☆ |")
    print("    | ☆                    ☆ |")
    print("    | ☆      3) Clock      ☆ |")
    print("    | ☆                    ☆ |")
    print("    | ☆     4) Weather     ☆ |")
    print("    | ☆                    ☆ |")
    print("    | ☆    5) Power Off    ☆ |")
    print("    | ☆                    ☆ |")
    print("     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")


while areWeDone == False:
    osMenu()
    desire = input("Which of the following features would you like to check: ")

    if desire.lower() == 'calculator':
        calculation()
    elif desire.lower() == 'notepad':
        writeNotes()
    elif desire.lower() == 'clock':
        displayTime()
    elif desire.lower() == 'weather':
        getWeather()
    else:
        finalSay = input("Are you sure you want to power off (y/n): ")
        if finalSay.lower() == 'y':
            break
        else:
            continue
    


print("Powering Off: ")

animation = [" ■□□□□□□□□□"," ■■□□□□□□□□", " ■■■□□□□□□□", " ■■■■□□□□□□", " ■■■■■□□□□□", " ■■■■■■□□□□", " ■■■■■■■□□□", " ■■■■■■■■□□", " ■■■■■■■■■□", " ■■■■■■■■■■"]

for i in range(len(animation)):
    time.sleep(0.4)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
