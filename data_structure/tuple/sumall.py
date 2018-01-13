# Many of the built-in functions use variable-length argument tuples. For example, 
# max and min can take any number of arguments:
print(max(1,2,3))
# But sum does not

# Write a function called sumall that takes any 
# number of arguments and returns their sum.

def sumall(*args):
	res = 0
	for item in args:
		res += item
	return res

test = sumall(1,2,3)
print(test)