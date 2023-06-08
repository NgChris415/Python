#print all integers from 0 to 150
i = 0
while i <= 150:
    print(i)
    i += 1

#print all multiples of 5 from 5 to 1,000
i = 5
while i <= 1000:
    print(i)
    i += 5

#print integers 1 to 100, if divible by 5 print "coding" instead. 
# If divisible by 10, print "Coding Dojo"
i = 1
while i <= 100:
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
    i += 1

#Add odd integers from 0 to 500,000 and print the final sum
i = 0
sum_of_odds = 0
while i <= 500000:
    if i % 2 == 1:
        sum_of_odds = i + sum_of_odds
    i += 1
print(sum_of_odds)

#print positive numbers starting at 2018, counting down by fours
for i in range(2018, 0, -4):
    if i % 2 == 0:
        print(i)

#set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of of mult. 
# for example lowNum= 2, high num= 9, and mult = 3, the loop should print 3,6,9

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)
