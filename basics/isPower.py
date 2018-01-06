def isPower(a, b):
	if a == 0:
		return False
	if b == 0:
		return False
	if a % b == 0:
		return True
	elif a % b != 0:
		return isPower(a / b, b)
	else:
		return false

print(isPower(8,0))