try:
    sum = 1 + '1'
    f = open('text.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('Error of file, reason is: ' + str(reason))
except TypeError as reason:
    print('Type Error, reason is: ' + str(reason))