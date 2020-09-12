#Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  count = 0
  check = []
  for letter in word:
    if letter in letters and not letter in check:
      count += 1
      check.append(letter)
  return count

print('Tests: Unique letters')
print('--------------')
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("purlpe"))
print(unique_english_letters("Axelander"))
print(unique_english_letters("Add"))

# Count X:
def count_char_x(word, x):
  count = 0 
  for letter in word:
    if letter in x:
      count += 1
  return count
# Tests:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Count Multi X:
def count_multi_char_x(word, x):
  count = word.count(x) 
  return count
# Note: I forgot about the count() function. 
# Tests:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
print(count_multi_char_x("Mike", "pp"))
# should print 0

# Count Multi X refactored:
def count_multi_char_x_rf(word, x):
  split = word.split(x)
  return len(split) - 1
# Notes: I wanted to use string functions even though my last solution worked. this is more clever and a more efficent solution.
# Tests:
print(count_multi_char_x_rf("mississippi", "iss"))
# should print 2
print(count_multi_char_x_rf("apple", "pp"))
# should print 1
print(count_multi_char_x_rf("Mike", "pp"))
# should print 0


# Substring Between:
def substring_between_letters (word, start, end):
  st = word.find(start)
  en = word.find(end)
  if st == -1 or en == -1:
    return word
  else:
    return word[st + 1:en]
# Tests:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# X Length:
def x_length_words(sentence, x):
  split = sentence.split()
  for word in split:
    if len(word) >= x:
      return True
    return False

# Tests:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


# Check Name:
def check_for_name(sentence, name):
  name_lst = [name.lower(), name.upper(), name.title()]
  for check in name_lst:
    if sentence.find(check) > -1:
      return True
  return False
   
# Tests:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# Every Other Letter:
def every_other_letter(word):
  return word[0:len(word):2]

# Tests:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 


# Reverse:
def reverse_string(word):
  lst = []
  index = -1
  for letter in word:
    lst += word[index]
    index -= 1
  return ''.join(lst)

# Tests:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

#  Reverse Refactored:
def reverse_string_rf(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
#Note: This is a good example of how to go backwords through a list using range() and len().
# Tests:
print(reverse_string_rf("Codecademy"))
# should print ymedacedoC
print(reverse_string_rf("Hello world!"))
# should print !dlrow olleH
print(reverse_string_rf(""))
# should print

# Reverse Refactored2:
def reverse_string_rf2(word):
  reverse = [i for i in word[::-1]]
  return ''.join(reverse)
  

# Tests:
print(reverse_string_rf2("Codecademy"))
# should print ymedacedoC
print(reverse_string_rf2("Hello world!"))
# should print !dlrow olleH
print(reverse_string_rf2(""))
# should print


# Reverse Refactored3:
def reverse_string_rf3(word):
  lst = ''
  for i in range(1 ,len(word)+1):
    lst += word[-i]
  return lst
# Tests:
print(reverse_string_rf3("Codecademy"))
# should print ymedacedoC
print(reverse_string_rf3("Hello world!"))
# should print !dlrow olleH
print(reverse_string_rf3(""))
# should print


# Make Spoonerism:
def make_spoonerism(word1, word2):
  return ' '.join((word2[0] + word1[1:] , word1[0] + word2[1:]))

# Tests:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# Add Exclamation:
def add_exclamation(word):
  while len(word) < 20:
    word += '!'
  return word
#Note: I couldn't tell that this was a call for a while loop...
# Tests:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn