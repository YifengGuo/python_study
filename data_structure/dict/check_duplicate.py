def has_duplicate(_list):
	d = {}
	for item in _list:
		if item not in d:
			d[item] = 1
		else:
			d[item] += 1
	for value in d.values():
		if value > 1:
			return True
	return False

_list = [1, 2, 3]
print(has_duplicate(_list))


