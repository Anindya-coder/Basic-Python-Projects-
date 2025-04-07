#this is a sample calculator program that perform calculation on two numbers
#it performs additioon, subtraction, multiplication, division and remainder

#calculator display
def calculatordisplay():
    display="""Welcome to the calculator 
    choose the operation you want to perform:
    1. addition
    2. subtraction
    3. multiplication
    4. division
    5. remainder
    6. exit
    """
    return display 

#operation input
def operationinput(userinput): 
    if userinput == 1:
        return 'initializing addition' 
    elif userinput == 2:
        return 'initializing subtraction'
    elif userinput==3:
        return 'initializing multiplication'
    elif userinput == 4:
        return 'initializing division'
    elif userinput==5:
        return 'initializing remainder'
    elif userinput>=6:
        return 'thanks for using'
    
#use input  
def getuserinput():
    while True:
        try:
            a = int(input('Enter the first non‑negative number: '))
            if a < 0:
                print("❌ Number must be zero or positive. Try again.")
                continue
            b = int(input('Enter the second non‑negative number: '))
            if b < 0:
                print("❌ Number must be zero or positive. Try again.")
                continue
            return a, b
        except ValueError:
            print("❌ Invalid input. Please enter whole numbers only.")
            continue
        
#calculator functions
def addition(a,b):
    return a+b 
def subtraction(a,b):
    return a-b 
def multiplication(a,b):
    return a*b 
def division(a,b):
    if b==0:
        return 'division by zero is not allowed'
    return a/b 
def remainder(a,b):
    if b==0:
        return 'division by zero is not allowed'
    return a%b

#main function to run the calculator
def runcalculation(): 
    while True:
        print(calculatordisplay())
        try:
            userinput=int(input('please enter the operation you want to perform(1-6)'))
        except ValueError:
            print('invalid input, please enter a number between 1 and 6')
            continue
        if userinput ==6:
            print('thanks for using')
            break
        print(operationinput(userinput))    
        try:
            a,b=getuserinput()
        except ValueError:
            print('invalid input, please enter a number')
            continue
        if userinput==1:
            print(f'addition of {a} and {b} is {addition(a,b)}')
        elif userinput==2:
            print(f'subtraction of {a} and {b} is {subtraction(a,b)}')
        elif userinput==3:
            print(f'multiplication of {a} and {b} is {multiplication(a,b)}')
        elif userinput==4:
            print(f'division of {a} and {b} is {division(a,b)}')
        elif userinput==5:
            print(f'remainder of {a } and {b} is {remainder(a,b)}')
        else:
            print('invalid input, please enter a number between 1 and 6')
            continue
        cont=input('Do you want to continue? (y/n)').strip().lower()
        if cont=='y':
            print('thank you')
            continue
        elif cont=='n':
            print('thanks for using')
            break
        else:
            print('invalid input, please enter y or n')
            continue 
if __name__=='__main__':
    runcalculation()

#program end