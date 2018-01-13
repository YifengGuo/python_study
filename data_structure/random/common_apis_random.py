import random

for i in range(10):
	x = random.random()
	print(x)

# The function randint takes parameters low and high and 
# returns an integer between low and high (including both).
for i in range(10):
	x = random.randint(5, 10)
	print(x)

# To choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
print('\n%d'%random.choice(t))