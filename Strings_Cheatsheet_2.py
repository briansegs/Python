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

# Count X
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