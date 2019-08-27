

print('Welcome to the guessing game')

name=input('whats your name? ')

import random
number= random.randint(1,50)

print('Hello', name, 'im thinking of a number between 1 and 100, you get 10 guesses')

no_guesses = 0

while no_guesses<5:

    print('take a guess ')
    guess= int(input())

    no_guesses+=1

    if guess=='':
        print('You have not entered a number ')
        no_guesses-=1

    if guess<number:
        print('too low, try again')
#now work out the next part
    if guess>number:
        print('too high, try again')

    if guess==number:
        print('Well done, you guessed in', no_guesses, 'tries')
        break

if guess!=number:
    print('too bad, the number i was thinking of is', number) 

else:
    print('Would you like to play again? ')
