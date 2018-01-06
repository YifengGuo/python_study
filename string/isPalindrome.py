def is_palindrome(s):
	if len(s) == 1 or len(s) == 0:
		return True
	elif s[0] != s[-1]:
		return False
	elif s[0] == s[-1]:
		return is_palindrome(s[1:-1])
	else:
		return False

print(is_palindrome('aaa'))



# version 2: use slice

def is_palindrome2(s):
	return s[::] == s[::-1]

print(is_palindrome2('aaab'))