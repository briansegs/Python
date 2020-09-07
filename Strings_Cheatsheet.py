#My first attempt
def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = ""
  new_name = username[-1] + username[:len(username) - 1]
  for i in new_name:
    password += i
  return password
#This solution didn't fully solve the problem but it passed the lesson. 

#Refactored
def username_generator_rf(first_name, last_name):
  if len(first_name) <= 3:
    username = first_name + last_name[:4]
  if len(last_name) <= 4:
    username = first_name[:3] + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username
#Note: turns out that Python handels slicing "gracefully" so this code was unnessary and my first attempt works better. No out of bounds errors.
#Test
print(username_generator('Ned','Red'))
print(username_generator('Shroom','Bloom'))

print(username_generator_rf('Al','Q'))
print(username_generator_rf('Abe','Simpson'))

def password_generator_rf(username):
  password = ""
  for index in range(len(username)):
    password += username[index - 1] 
  return password
#Test
print(password_generator_rf('NedRed'))
print(password_generator_rf('ShrBloo'))
print(password_generator_rf('AlQ'))
print(password_generator_rf('AbeSimp'))

#Splitting Strings II: 
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')
print(author_names)
print('_____')

n = authors.split(' ')
print(n)
author_last_names = []
for name in n:
  if name[-1] == ',':
    author_last_names.append(name[:-1])
  if name == n[-1]:
    author_last_names.append(name)

print('_____') 
print(author_last_names)
expected_output = ['Lorde', 'Williams', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']
assert author_last_names == expected_output
#Note: Having to find the pattern in the string and then make code around it was fun.
#Note: Solving how to deal with the last name in the list breaking the pattern was challenging but also fun.

#Splitting Strings II: Refactored
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

expected_output = ['Lorde', 'Williams', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']
assert author_last_names == expected_output
#Note: I didn't get why this worked. I had to rubber duck my way through it. It's a better solution

#Splitting Strings II: Refactored2 (Kat's request)
author_last_names = [name.split()[-1] for name in author_names]

expected_output = ['Lorde', 'Williams', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']
assert author_last_names == expected_output
