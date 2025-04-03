import random 
while True:
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    choice=input('Roll the dice? (y/n): ')
    if choice =='y':
        print(f'{die1},{die2}')
    elif choice =='n':
        print('thanks for playing')
        break 
    else:
        print('invalid choice')
        continue
