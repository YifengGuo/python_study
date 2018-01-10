def fibonacci(n):
	# base case
	a = 0
	b = 1
	i = 0
	res = 0
	while i < n:
		c = a + b
		a = b
		b = c
		i += 1
	return a
print(fibonacci(5))

# 0 1 1 2 3 5 8

# use dict
def fibonacci2(n):
	# base case
	known = {0:0, 1:1}
	if n in known:
		return known[n]
	res = fibonacci2(n - 1) + fibonacci2(n - 2)
	known[n] = res
	print(known)
	return res

print(fibonacci2(5))