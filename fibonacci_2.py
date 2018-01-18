def fab(n):
    if n < 1:
        print('wrong number')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

number = int(input('please entrer numbers of rabbits at beginning: '))
result = fab(number)
print('There are %d pairs rabbits were borned' % result)
