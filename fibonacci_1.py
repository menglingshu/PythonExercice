def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('wrong number')
        return -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

number = int(input('please entrer numbers of rabbits at beginning: '))
result = fib(number)
if result != -1:
    print('There are %d pairs rabbits were borned' % result)
    
