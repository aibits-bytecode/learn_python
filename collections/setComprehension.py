numbers = [1,2,3,4,5,3,4,5,6,7,8,9]
set1 = set(numbers)
print(set1)
# in here we can see set does not allow duplicate numbers

even = [i for i in set1 if i%2==0]
print(even)