def is_anagram(s1, s2):
	if len(s1) != len(s2):
		return False
	for char in s1:
		if char not in s2:
			return False
	for char in s2:
		if char not in s1:
			return False
	return True

s1 = 'apple'
s2 = 'kplea'

print(is_anagram(s1, s2))