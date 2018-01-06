def is_reverse(s1, s2):
	if len(s1) != len(s2):
		return False

	i = 0
	j = len(s2) - 1
	while j > 0:
		if s1[i] == s2[j]:
			j -= 1
			i += 1
		else:
			return False
	return True

s1 = 'pots'
s2 = 'stoe'
print(is_reverse(s1, s2))