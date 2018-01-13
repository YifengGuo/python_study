import string
def process_file(filename):
	h = {}
	fp = open(filename)
	for line in fp:
		process_line(line, h) # process each line of the article
	return h

def process_line(line, h):
	line = line.replace('-', ' ') # replace hyphens with whitespaces

	for word in line.split(): # break line into list of strings
		word = word.strip(string.punctuation + string.whitespace) # remove punctuations and whiletespaces
		word = word.lower() # to lower case

		h[word] = h.get(word, 0) + 1

# find most common words
def find_most_common(h):
	res = []
	for key, value in h.items():
		res.append((value, key)) # append pair as tuple into list

	res.sort(reverse=True) # sort the list by descending order of value

	# find top 10 most common words in the dict
	print('The top 10 most common words are:')
	for freq, word in res[0 : 10]:
		print(word, '\t', freq)


find_most_common(process_file('austen-emma.txt'))