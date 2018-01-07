def chop(my_list):
	if len(my_list) <= 0:
		return
	if len(my_list) == 1:
		del my_list[0]
		return
	del my_list[0]
	del my_list[len(my_list) - 1]

# test chop()
l1 = [1, 2, 3, 4, 5, 6]
l2 = []
l3 = [1]
l4 = [1, 2]
l5 = [1, 3, 5]
lists = []
lists.append(l1)
lists.append(l2)
lists.append(l3)
lists.append(l4)
lists.append(l5)
print('test chop()')
for _list in lists:
	chop(_list)
	print(_list)


def middle(my_list):
	if len(my_list) <= 0:
		return []
	res = my_list[1:-1]
	return res

# test middle()
l1 = [1, 2, 3, 4, 5, 6]
l2 = []
l3 = [1]
l4 = [1, 2]
l5 = [1, 3, 5]
lists = []
lists.append(l1)
lists.append(l2)
lists.append(l3)
lists.append(l4)
lists.append(l5)
print('test middle()')
for _list in lists:
	res = middle(_list)
	print(res)

