import os
import time

def writeNotes():

    seconds = time.time()
    local_time = time.ctime(seconds)

    print()

    checking = input("Hello, would you like to enter an entry into the journal (y/n): ")

    if checking.lower() == 'y':
        print('\nYour entry will be saved into your notepad that can be accessed at any time.\n')
        entry = input("Write your entry: ")

        # Use os module to get the user's home directory
        home_dir = os.path.expanduser("~")
        desktop_dir = os.path.join(home_dir, "Desktop")

        # Specify the filename
        filename = os.path.join(desktop_dir, "NotePad.txt")

        with open(filename, "a") as myFile:  #with automatically closes the file after its done
            myFile.write(str(local_time) + "\n")
            myFile.write(str(entry) + '\n\n')
    else:
        print("\nOkay, what would you like to do next?\n")


writeNotes()
