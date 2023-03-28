# set is unordered collection of unique elements
# unordered, so we are not able to access by index

# in here we can see this is a set
set1 = set()
print(type(set1))

# in here we can see this is a dictionary so when initialize set use previous method
set2 = {}
print(type(set2))

# frozensets does not allow to change the set
numbers = [1,2,3,3,4,5,3,3,2]
fset1 = frozenset(numbers)
print(fset1)
# you can check the values are in sets/frosenset by this
print(1 in fset1)
