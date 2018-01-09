def invert_dict(d):
	value_to_key = {}
	for key in d:
		v = d[key]
		if v not in value_to_key:
			value_to_key[v] = [key]
		else:
			value_to_key[v].append(key)
	return value_to_key

s = 'sjadidjsjdiwjf'
d = {}
for char in s:
	if char not in d:
		d[char] = 1
	else:
		d[char] += 1 
inverted_d = invert_dict(d)
print(inverted_d)