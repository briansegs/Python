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

