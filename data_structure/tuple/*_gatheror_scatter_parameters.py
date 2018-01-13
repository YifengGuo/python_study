# A parameter name begins with * gathers arguments into a tuple
def printall(*args):
	print(args)

printall(1, '2', [1, 2, 3])

# If you have a sequence of values and you want to pass it to a function as multiple arguments, 
# you can use the * operator
t = (7, 3)
print(*t)
res = divmod(*t)
print(res) # (2, 1))