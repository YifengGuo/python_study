d = {}
s = 'jsaidjjdsadawe'
for char in s:
	if char not in d:
		d[char] = 1
	else:
		d[char] += 1


def reverse_lookup(d, v):
	res = []
	for key in d:
		if d[key] == v:
			res.append(key)
	return res

print(reverse_lookup(d, 3))
