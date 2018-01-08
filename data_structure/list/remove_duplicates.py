# 1 2 3 4 5 5 
#           f
#          s
def deduplicate(_list):
	_list.sort()
	slow = 0
	for fast in range(len(_list)):
		if _list[fast] == _list[slow]:
			continue
		else:
			slow += 1
			_list[slow] = _list[fast]
	return _list[:slow+1]

_list = [1, 3, 5, 2, 6, 2, 3]
print(deduplicate(_list))