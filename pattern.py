#outer loop defines the number of lines 
#inner loop defines the number of elemes in each line

#patter 1
#*****
#*****
#*****
#***** 
for i in range(4):
    for j in range(5):
            print('*', end='')        
    print()
    
#pattern 2 
#1 2 3 
#4 5 6
#7 8 9


i = 1
j=1
num =1
for i in range(3):
    for j in range(3):
        print(num, end=' ')
        num+=1
    print()

#pattern 3 
#A B c D 
#E F G H 
#I J K L
#M N O P

char = 'A'
for i in range(4):
    for j in range(4):
        print(char,end=' ')
        char = chr(ord(char)+1)
    print()
    
#pattern 4 
#*
#* *
#* * *
#* * * * 

i=0
j=0 
for i in range(4):
    for j in range(i+1):
        print('*',end=' ')
    print()
    
#pattern 5 
#1 
#2 2 
#3 3 3 
#4 4 4 4 

i=0
j=0 
for i in range(4):
    for j in range(i+1):
        print(i+1,end=' ')
    print()