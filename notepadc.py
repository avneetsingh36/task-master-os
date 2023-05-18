import time
import os

def writeNotes():

    seconds = time.time()
    local_time = time.ctime(seconds)

    print()

    print('\nYour entry will be saved into your notepad that can accessed at any time.\n')
    entry = input("Write your entry: ")

    # Determine path to desktop
    desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
    filename = os.path.join(desktop, 'NotePad.txt')

    with open(filename, "a") as myFile:  #with automatically closes the file after its done
        myFile.write(str(local_time) + "\n")
        myFile.write(str(entry) + '\n\n')


    goAgainNotes = input("Would you like to write another note (y/n): ")

    if goAgainNotes.lower() == "y":
        writeNotes()
    else:
        print("\nOkay, what would you like to do next?\n")
