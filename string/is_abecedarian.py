# to determine if each character in a string
# is in ascending order


# method 1 use for loop
def is_abecedarian_1(s):
	prev = s[0]
	for char in s:
		if char < prev:
			return False
		prev = char
	return True

# method 2 use recursion
def is_abecedarian_2(s):
	# base case: only one character in the string
	if len(s) <= 1:
		return True
	# comparion between two characters
	if s[0] > s[1]:
		return False
	# recurse from 1:end substring
	return is_abecedarian_2(s[1:])

# method 3 use while loop
def is_abecedarian_3(s):
	i = 0
	while i < len(s) - 1:
		if s[i] > s[i+1]:
			return False
		i += 1
	return True

# test
s1 = 'abcdefgh'
s2 = 'bcdfghia'

print(is_abecedarian_1(s1))
print(is_abecedarian_2(s1))
print(is_abecedarian_3(s1))
print(is_abecedarian_1(s2))
print(is_abecedarian_2(s2))
print(is_abecedarian_3(s2))

