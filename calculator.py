
def constructCalc(answer):
    
    print()
    print(f"|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|")    
    print(f"| A/C | +/- |  %  |  /  |")
    print(f"|     |     |     |     |")
    print(f"|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|")
    print(f"|  1  |  2  |  3  |  X  |")
    print(f"|     |     |     |     |")
    print(f"|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|")
    print(f"|  4  |  5  |  6  |  -  |")
    print(f"|     |     |     |     |")
    print(f"|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|")
    print(f"|  7  |  8  |  9  |  +  |")
    print(f"|     |     |     |     |")
    print(f"|‾‾‾‾‾ ‾‾‾‾‾|‾‾‾‾‾|‾‾‾‾‾|")
    print(f"|   0       |  .  |  =  |")
    print(f"|           |     |     |              | Answer: {answer} | ")
    print(f" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
answer = 0

def calculation():
    global answer
    bp = 0
    nums = ''
    fh = ''
    bp = 0
    sign = ''
    num1 = ''
    num2 = ''

    constructCalc(answer)

    equation = input("Enter the funtion would you would like to solve (separate with spaces): ")
    equation = list(equation)

    for i in equation:
        if i.isnumeric() == True or (i == ' '):
            nums = str(nums) + str(i)
        if i.isnumeric() == False and (i != ' '):
            sign = i
    fh = list(nums)
    for i in fh:
        bp += 1
        if int(i.isnumeric()) == True:
            num1 = num1 + i
        else:
            break
    num1 = int(num1)  
    length = len(nums)
    num2 = int(nums[bp:length])


    def d(num1, num2):
        global answer
        answer = float(num1) / float(num2)

    def m(num1, num2):
        global answer
        answer = float(num1) * float(num2)

    def s(num1, num2):
        global answer
        answer = float(num1) - float(num2)

    def a(num1, num2):
        global answer
        answer = float(num1) + float(num2)
    
    if sign == "x" or sign == "X":
        m(num1,num2)
    elif sign == "/":
        d(num1,num2)
    elif sign == '+':
        a(num1,num2)
    elif sign =='-':
        s(num1,num2)
    else:
        print("You entered faulty input!")

    constructCalc(answer)

    goAgain = input("Would you like to perform another calculation (y/n): ")
    if goAgain.lower() == "y":
        print('\n\n\n')
        calculation()
    else:
        print("\nOkay, what would you like to do next?\n")

