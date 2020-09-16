def checkPalindrome(word):
    check = -1
    for letter in word:
        if letter == word[check]:
            check += -1
        else:
            return False
    return True    
    
    
print(checkPalindrome('aabaa'))    