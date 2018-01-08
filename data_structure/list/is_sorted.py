def is_sorted(_list):
	for i in range(len(_list) - 1):
		if _list[i] > _list[i + 1]:
			return False
	return True

l1 = [1, 2, 2, 1]
l2 = ['b', 'a']

print(is_sorted(l1))
print(is_sorted(l2))