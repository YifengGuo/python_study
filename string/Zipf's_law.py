# -*- coding: utf-8 -*-
# Zipf’s law describes a relationship between the ranks and frequencies of words
# in natural languages.
# Specifically, it predicts that the frequency, f , of the word with rank r is:
#                        f = cr^(-s)
# where s and c are parameters that depend on the language and the text. 
# If you take the logarithm of both sides of this equation, you get:
#                        logf = logc - s*logr
# So if you plot log f versus log r, 
# you should get a straight line with slope −s and intercept log c.
import string
import numpy as np
import matplotlib.pyplot as plt

# step 1： count word frequency
def word_freq(filename):
	d = {}
	fp = open(filename)
	for line in fp:
		process_line(line, d)
	return d


def process_line(line, d):
	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		# ignore whitespace
		if word != '':
			d[word] = d.get(word, 0) + 1


def sort_dict_by_freq(d):
	res = []
	for word, freq in d.items():
		res.append((freq, word))
	res.sort(reverse=True)
	return res

def calc_log(l):
	res = []
	for i in range(len(l)):
		word = l[i][1]
		freq = l[i][0]
		rank = i + 1
		# print '%s %d %f %f' %(word, freq, np.log(freq), np.log(rank))
		res.append((np.log(freq), np.log(rank)))
	return res


filename = 'austen-emma.txt'
d = word_freq(filename)
# for word, freq in d.items():
# 	print(word, freq)
l = sort_dict_by_freq(d)
res = calc_log(l)
print res

for f, r in res:
	plt.scatter(f, r)
plt.show() # logf = logc − slogr which is a straight line