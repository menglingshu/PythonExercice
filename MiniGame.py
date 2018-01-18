import random

secret = random.randint(1, 10)

print('------- i love uc studio -------')

for i in range(0,3):
    temp = input('You have 3 chances~ Please guess a number: ')
    guess = int(temp)
    if guess > secret:
        print('Guess fail It\'s too big')
    elif guess==secret:
        print('Wooow you re right')
        break
    else:
        print('Guess fail it\'s too small')    
        
print('game over bye')
