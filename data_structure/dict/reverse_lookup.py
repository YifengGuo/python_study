d = {}
s = 'jsaidjdsadawe'
for char in s:
	if char not in d:
		d[char] = 1
	else:
		d[char] += 1


def reverse_lookup(d, v):
	for key in d:
		if d[key] == v:
			return key
	raise ValueError

print(reverse_lookup(d, 3))
