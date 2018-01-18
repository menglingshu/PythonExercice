def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y) #move n-1 plate from x to y
        print(x, '-->', z) #move last plate in the bottom from x to z
        hanoi(n-1, y, x, z) #move n-1 plate that on y, put on z

n = int(input('please entrer floors of hanoi: '))
hanoi(n, 'X', 'Y', 'Z')
