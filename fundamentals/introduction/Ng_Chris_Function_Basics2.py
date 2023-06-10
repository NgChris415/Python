#1 create a function that acceps a number as an input. return a new list that counts down by 1
#from the number as the 0th elment down to 0 as the last element
#examople countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    while num >= 0:
        print(num)
        num -= 1
countdown(5)

#2 create a function that acceps a list and returns the sum of the first value in the list plus
#the list's length
#example print_and_return([1,2]), shoulder print 1 and return 2

listy = [1,2]
def print_and_return(list):
    print(list[0])
    return(len(list))
print_and_return(listy)
print(len(listy)) #just to test in console to make sure it returns the correct number 

#3 create a function that acceps a list and returns the sum of the first value in the list 
# plus the list's length.
#example: first_plus_length([1,2,3,4,5]) should return 6

listy2 = [1,2,3,4,5]
def first_plus_length(list2):
    print(list2[0] + len(list2))
    return(list2[0] + len(list2))
first_plus_length(listy2)

#4 write a function that accepts a list and creates a new list containing
#only values from the original list that are greater than its 2nd value
# print how many values this is and then return the new list. if the list has less than
# 2 elements, have the function return false
# example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# example: values_greater_than_second([3]) should return false

listy3 = [5,2,3,2,1,4]
listy4 = [3]
listy5 = []

def values_greater_than_second(list3):
    if len(list3) < 2:
        return("false")
    else:
        print(len(list3))
        i = 0
        while i < len(list3):
            if list3[i] > list3[1]:
                listy5.append(listy3[i])
            i += 1

print(values_greater_than_second(listy3))
print(values_greater_than_second(listy4))
print(listy5)

#5 write a function that accepts two integers as parameters: size and value. the function should
# create and return a list whose length is equal to the given size, and whose values are all the 
# given value
# example: length_and_value(4,7) should return [7,7,7,7]
# example: length_and_value(6,2) shoulde return [2,2,2,2,2,2]

listy6 = []

def length_and_value(length, value):
    i = 0
    while i <= length:
        listy6.append(value)
        i += 1 
length_and_value(4,7)
print(listy6)