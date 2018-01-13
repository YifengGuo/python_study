# combinations between dict and tuple
# items() (or entrySet() in Java)
# 
# Dictionaries have a method called items that returns a list of tuples, 
# where each tuple is a key-value pair2 .
d = {'a':0, 'b':1, 'c':2}
print(type(d.items()))
print(d.items()) # list of tuples

# and conversely using list of tuples can 
# initialize a new dict
t = [('a', 0), ('c', 2), ('b', 1)] 
d = dict(t) # initialze new dict
print(d) # new dict

# Combining dict with zip yields a concise way to create a dictionary
d = dict(zip('abc', range(3)))
print(d)

for key, value in d.items():
	print(key, value)

# because tuples are immutable, and lists are
# mutable, so we can apply tuples as keys in Dictionaries
# for example ('firstname', 'lastname') -> (telephone number)
user1 = ('John', 'Andyson')
user2 = ('William', 'Kaily')
tele1 = '732-123-123'
tele2 = '732-123-321'
d = {}
d[user1] = tele1
d[user2] = tele2
print(d)