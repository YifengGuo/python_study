def count(s, letter):
	count = 0
	for char in s:
		if char == letter:
			count += 1
	return count

print(count('mathmatica', 'm'))