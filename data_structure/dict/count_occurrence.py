def count_occurrence(s):
	d = {}
	for char in s:
		if char not in d:
			d[char] = 1
		else:
			d[char] += 1
	return d

s = 'sajidjaiwdsid'
d = count_occurrence(s)
for key in d:
	print('%s : %d' %(key, d[key]))