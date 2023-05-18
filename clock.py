import datetime




def displayTime():
    e = datetime.datetime.now()

    print('\n\nCurrent Time: ')


    hour = e.hour
    minute = e.minute
    print(f'Date: {e.month}/{e.day}/{e.year}')
    print(f'Time: {hour}:{minute}\n')

    goAgainTime = input("Would you like check the time again (y/n): ")

    if goAgainTime.lower() == "y":
        displayTime()
    else:
        print("\nOkay, what would you like to do next?\n")

    
