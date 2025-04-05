import random 
def getRandomnumber():
    return random.randrange(1,100,1)

def givehints(guess,number):
    if guess < number:
        return 'cold'
    elif guess > number:
        return 'hot'
    else:
        return 'right'

def runguess():
    secret_number = getRandomnumber()
    while True:
        userguess = int(input('guess a number between 1 and 100: '))
        hint=givehints(userguess,secret_number)
        if hint == 'right':
            print('congratulations')
            break
        else:
            print(hint)
            if hint == 'cold':
                print('try a higher number')
            else:
                print('try a lower number')

if __name__== "__main__":
    runguess()