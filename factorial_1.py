def factorial(x):
	result = x
	for i in range(1, x):
		result *= i
	return result
number = int(input('please entrer a number: '))
result = factorial(number)
print('factorial of %d is: %d' % (number, result))
