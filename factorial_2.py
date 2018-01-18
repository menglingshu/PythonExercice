def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('please entrer a number: '))
result = factorial(number)
print('The factorial of %d is: %d' % (number, result))
