# The comparison operators work with tuples and other sequences; 
# Python starts by comparing the first element from each sequence. 
# If they are equal, it goes on to the next elements, and so on, 
# until it finds elements that differ. 
tuple1 = (0, 1, 2)
tuple2 = (0, 3, 4)
print(tuple1 < tuple2) # True

tuple3 = (0, 1, 200000)
tuple4 = (0, 3, 4)
print(tuple3 < tuple4) # True

# The sort function works the same way. 
# It sorts primarily by first element, but in the case of a tie, 
# it sorts by second element, and so onself. 
f = open('/Users/guoyifeng/PycharmProjects/python_study/words.txt')
words = []
for i in range(1000):
	words.append(f.readline().strip('\n'))
f.close()
# print(words)

def sort_by_length(words):
	temp = []
	for word in words:
		temp.append((len(word), word))

	temp.sort(reverse=True) # sorted in descending order
	res = []
	for length, word in temp: # first compare length, and compare
	                          # lexicographical order
		res.append(word)

	return res


res = sort_by_length(words)
print(res)