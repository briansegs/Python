#Given the string, check if it is a palindrome.
def checkPalindrome(word):
    check = -1
    for letter in word:
        if letter == word[check]:
            check += -1
        else:
            return False
    return True    
    
print(checkPalindrome('aabaa'))    


#Write a function that returns the sum of two numbers.
def add(param1, param2):
    return param1 + param2

print(add(250, 128))


#Given a year, return the century it is in. 
import math
def centuryFromYear(year):
    return math.ceil(year / 100)

print(centuryFromYear(1986))


#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
def adjacentElementsProduct(lst): 
    large_num = lst[0] * lst[1]
    for index in range(1, len(lst) - 1):
        check = lst[index] * lst[index + 1]
        if check > large_num:
            large_num = check
    return large_num

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))


#Below we will define an n-interesting polygon.
def shapeArea(n):
    return (n - 1)**2 + n**2

print(shapeArea(5))


#The minimal number of statues that need to be added to existing statues.
def makeArrayConsecutive2(statues):
    return len([num for num in range(min(statues), max(statues)) if num not in statues])

print(makeArrayConsecutive2([6, 2, 3, 8]))

