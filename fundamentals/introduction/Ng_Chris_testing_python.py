import random

print('Welcome to Python!') #log statement, strings

print('This is a loop printing 5 times') #log statement
for x in range(1, 6): #for loop, numbers, variable declaration
    print(f'x is: {x}') #log statement, string interpolation

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #list
day = random.choice(weekdays) 

print(f'Today is: {day}') #log statement, string interpolation

if day == 'Monday': #conditional
    print('It will be a long week!') #log statement, string
elif(day == 'Friday'): #conditional
    print('Woohoo, time for the weekend!') #log statement, string
else: #conditional
    print('Not quite there yet.') #log statement, string
