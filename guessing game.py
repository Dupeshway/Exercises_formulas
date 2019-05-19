#Learn the terms for the characters

print('Welcome to the guessing game!')

name = input('Whats your name? ')

print('Hello', name,' lets play the guessing game!')

import random

startno=0
endno=100

number = random.randint(startno,endno)

guess_count = 0

print('Guess a number between', startno, 'and', endno)

while guess_count<10:

    guess_count+=1

    guess=int(input('\n Hit enter when done: '))

    if guess='':
        print('You didnt write anything, have another try')
        guess_count-=1
    
    if guess > number:
        print('Too high, guess again\n ')

    if guess < number:
        print('Too low, guess again\n ')

    if guess == number:
        print('Well done, you guessed in', guess_count, 'tries!\n')
        break

if guess!= number:
    print('Oh no! Youve run out of guesses, want to try again?')

else:
    print('Good job, wanna play again? ')
