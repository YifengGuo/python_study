# zip is a built-in function that takes two or more sequences 
# and “zips” them into a list of tuples where each tuple contains 
# one element from each sequence.
# In Python 3.0,zipreturns an iterator of tuples, but for most purposes, 
# an iterator behaves like a list.

# example 1:
s = 'abc'
l = [0, 1, 2]
res1 = zip(s, l)
print(type(res1)) # zip object
                  # list of tuples
# for item in res1:
# 	print(item)    # print in tuple

for letter, number in res1:
	print(letter, number)

# even lengths of two iterable objects
# are not identical, zip() can work as well

# example 2
# traverse two or more lists by zip and for
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 5]
def is_identical(l1, l2):
	for num1, num2 in zip(l1, l2):
		if num1 != num2:
			return False
	return True
print(is_identical(l1,l2))

# If you need to traverse the elements of a sequence and their indices, 
# you can use the built-in function enumerate
l3 = ['a', 'b', 'c']
for index, value in enumerate(l3):
	print(index, value)
# 0 a
# 1 b
# 2 c