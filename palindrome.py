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


#Palindrome refactored with recursive algorithm.

def checkPalindrome_r(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return checkPalindrome_r(word[1: -1])

print(checkPalindrome_r('aabaa')) 