# list() make ... into a list
s = 'spam'
list1 = list(s)
print(list1)


# string.split(): return a list
s = 'hello world'
list1 = s.split()
print(list1)

# delimiter: argument for spilt()
# to specify delimit the string by
# which character
s = 'what-is-that'
delimiter = '-'
res = s.split(delimiter)
print('type of splited string result: %s' % type(res))
print(res)

# join: reverse operation of split
# it takes a list of strings and concatenates
# the elements
my_list = ['It', 'is', 'a', 'thing']
delimiter = ' '
res = delimiter.join(my_list)
print(res)
print(type(res))

# strip()
s = '   it    is    a     thing    \n\n\n'
print(s.strip())

my_list = [1, 2, 3, 4, 5, 6]

my_list.append(7)
print(my_list) # append 7

del my_list[0] # without return value
print(my_list) # delete the first element of list

my_list.remove(2) # remove 2 from the list
print(my_list)

print(my_list.pop()) # pop() has return value
                     # pop(index), remove and return elemnt at ... index
                     # pop() remove and return last element in the list by default

# sort
l = [3, 25, 6, 21, 1, 52, 12]
l.sort() # sort() is void function,cannot assign another variable
print(l)

# append and +
print('\nappend and +:')
l1 = [1, 2, 3]
l2 = l1.append(4)
l3 = l1 + [4] # + operator creates a new list object
print(l1)
print(l2) # None for append() only modifies current list
print(l3)
