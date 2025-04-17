#outer loop defines the number of lines 
#inner loop defines the number of elemes in each line

#pattern 1
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
#pattern 6
#1 
#2 3 
#4 5 6 
#7 8 9 10 

i=0 
j=0
num =1
for i in range(4):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()
    
#pattern 7
#1
#1 2
#1 2 3
#1 2 3 4

i,j=0,1
for i in range(4):
    for j in range(i+1):
        j+=1
        print(j,end=' ')
    print()

#pattern 8
#1
#2 1
#3 2 1
#4 3 2 1

i=0
j=0
for i in range(4):
    for j in range(i+1):
        print(i-j+1,end=' ')
    print()

#pattern 9
#* * * *
#* * * 
#* *
#*
i,j=0,0
for i in range(4):
    for j in range(4-i):
        print('*',end=' ')
    for j in range(i):
        print(end=' ')
    print()

#pattern 10 
#1 1 1 1 
# 2 2 2 
#  3 3 
#   4
i,j=0,0
for i in range(4):
    for j in range(i):
        print(end=' ')
    for j in range(4-i):
        print(i+1,end=' ')
    print()
    
#pattern 11 
#    1
#   2 3
#  4 5 6
# 7 8 9 10
i,j,num=0,0,1
for i in range(4):
    for j in range(4-i-1):
        print(end=' ')
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()

#pattern 12 
#    1
#  1 2 1
# 1 2 3 2 1
#1 2 3 4 3 2 1 
i,j=0,0
for i in range(4):
    for j in range(4-i-1):
        print(end=' ')
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range(i):
        print(i-j,end=' ')
    print()
