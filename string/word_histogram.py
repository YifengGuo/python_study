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

filename = 'austen-emma.txt'
h = process_file(filename)
for pair in h.items():
	print(pair)

def total_words(h):
	return sum(h.values())

def different_words(h):
	return len(h)

print ('Total number of words:', total_words(h))
print ('Number of different words:', different_words(h))