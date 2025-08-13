# ------ Exercise 1

month = int(input('Enter a month (1-12): '))

if month in range(3, 6):
    print('Spring')
elif month in range(6, 9):
    print('Summer')
elif month in range(9, 12):
    print('Autumn')
elif month in (12, 1, 2):
    print('Winter')
else:
    print('This month does not exist')

# ------ Exercise 2
print('---- Exercices 2-1 ')
for i in range(1 , 21):
    print(i)
print('---- Exercices 2-2 ')
for i in range(1 , 21):
    if i % 2 == 0 :
        print(i)

# ------ Exercise 3

name = input('Enter your name : ')
while name != 'othmane':
    name = input('Enter your name : ')

# ------ Exercise 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input('Enter your name : ')
if(name in names):
    print(names.index(name))

# ------ Exercise 5
i = 1 

num = int(input(f'Enter 1st number : '))
numbers = [num]
while i != 3 : 
    num = int(input(f'Enter {i+1}st number : '))
    numbers.append(num)
    i+=1
print(f'The greatest number is: {max(numbers)}')

# ------ Exercise 6

import random 
rand_num = random.randint(1,9)
print(rand_num)
num = int(input(f'Enter numer between (1,9) : '))

while num != rand_num : 
     print('Better luck next time.')    
     num = int(input(f'Enter numer between (1,9) : '))
print('Winner')          
