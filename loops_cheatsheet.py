#Python For Loops
#for <temporary variable> in <list variable>:
#  <action statement>
#  <action statement>

#Counts items in list and checks if they can be divided by 10
def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i % 10 == 0:
      count += 1
  return count    

print(divisible_by_ten([20, 25, 30, 35, 40]))

#Appends string to items in a list 
def add_greetings(names):
  greetings = []
  greetings = ["Hello, " + name for name in names]
  return greetings
#Can also be written this way
def add_greetings_refactored(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)
  return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))

#Using a while loop and slicing to slice away any first number that is even
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
#Note: A while loop will leave you with an empty list in this example but a 'for loop' will leave you with 'none'
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Using range(), len(), and list indexing to make a new list of items that were in odd index locations of the old list 
def odd_indices(lst):
  new_lst = []
  new_lst = [lst[num] for num in range(1, len(lst), 2)]
  return new_lst
#can also be written...
def odd_indices_refactored(lst):
  new_lst = []
  for num in range(1, len(lst), 2):
    new_lst.append(lst[num])
  return new_lst
#Note:Using range() and len() together gives a reliable way to access the index locations of any list
#Note:list[1] gives you the item at that index location    
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Using nested loops to do math and make a new list
def exponents(bases, powers):
  new_lst = []
  for num1 in bases:
    for num2 in powers:
      new_lst.append(num1 ** num2)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))

#finding which list has the larger sum and returning that list
def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  for num in lst1:
    sum_lst1 += num
  for num in lst2:
    sum_lst2 += num
  if sum_lst1 >= sum_lst2:
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

def over_nine_thousand(lst):
  lst_sum = 0
  lst_count = 0
  for num in lst:
    lst_sum += num
    lst_count += 1
    if lst_sum > 9000 or lst_count >= len(lst):
      return lst_sum
  return 0

def over_nine_thousand_refactored(lst):
  lst_sum = 0
  for num in lst:
    lst_sum += num
    if lst_sum > 9000:
      break
  return lst_sum
#Notes: If a 'for loop' exits or doesen't start, the next code outside of the loop will run.
#Note: An empty list will not get looped through and cause the next line ot code to be exicuted.
#Note: If an 'if' statment doesn't get met, the next line of code will start.
#Note: If values were being recorded they can still be used if they are outside of the loop. 
#Testing...
print("Test 1: Expected value: 9020")
print(over_nine_thousand([8000, 900, 120, 5000]))
print("Test 2: Expected value: 1340 ")
print(over_nine_thousand([40, 100, 1000, 200]))
print("Test 3: Expected value: 0 ")
print(over_nine_thousand([]))
print("Test 4: Expected value: 9500")
print(over_nine_thousand([500, 3000, 1000, 5000]))
print("Test 5: Expected value: 1700")
print(over_nine_thousand([800, 900]))
# Assert for testing...
print("Using assert for test driven development")
assert over_nine_thousand([8000, 900, 120, 5000]) == 9020
assert over_nine_thousand([40, 100, 1000, 200]) == 1340
assert over_nine_thousand([]) == 0
assert over_nine_thousand([500, 3000, 1000, 5000]) == 9500
assert over_nine_thousand([800, 900]) == 1700
print("All tests passed!")

#My first solution...
def max_num(nums):
  lst = sorted(nums)
  return lst[-1]
#Notes:I came up with this knowing that it wasn't a loop but it did solve the problem. The problem with this solution is that it is very costly runtime wise. It is O(n log n).
#notes:The bigger the list get the more problems it will cause.
print(max_num([50, -10, 0, 75, 20]))

#second solution...
def max_num_refactored(nums):
  max_num = nums[0]
  for num in nums:
    if max_num < num:
      max_num = num
  return max_num
#This is a better solution because it is a loop and has a better runtime. O(n)
#I also think it is a good solution for finding things in lists
print(max_num_refactored([50, -10, 0, 75, 20]))

#Finding the index...
def same_values(lst1, lst2):
  same = []
  for num in range(len(lst1)):
    if lst1[num] == lst2[num]:
      same.append(num)
  return same    
#Note: I needed to find the loop count (item number 'num') to show the index 
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Check the front and back...
def reversed_list(lst1, lst2):
  check = -1
  for num in lst1:
    if num == lst2[check]:
      check += -1
    else:
      return False
  return True    
#Note: I stole the code i wrote for solving the palindronme problem to see if it would work for this problem. It worked the same way.
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))