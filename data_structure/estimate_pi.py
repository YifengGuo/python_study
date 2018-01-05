import math


def estimate_pi():
	factor = 2 * math.sqrt(2) / 9801
	epsilon = 10 ** (-15)
	temp = 0.0
	while True:
		k = 0
		temp += (factorial(4 * k) * (1103 + 26390 * k)) / (factorial(k) * 496 ** (4 * k))
		print(temp)
		if temp < epsilon:
			break
		k += 1
	return 1 / (factor * temp)

def factorial(n):
	if n == 0:
		return 1
	else:
		temp = factorial(n - 1)
		return n * temp

print(estimate_pi())

