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

