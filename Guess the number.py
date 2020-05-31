#This a guess the number game

import random

print('Hello. What is your name?')
name = input()

print('Hi ' + str(name) + ', Can you guess the number I am thinking of in six guesses? It is a number between 1 and 20.')
secretNumber = random.randint (1,20)

#print('Debug: Secret Number = ' + str(secretNumber))

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too high.')
    elif guess < secretNumber:
        print('Your guess is too low.')
    else:
        break #This condition is for the correct guess!

if guess == secretNumber:
    print('Well done ' + str(name) + ', you guessed the right number! You took ' + str(guessesTaken) + ' guesses.')

else:
    print('Nope, the number I was thinking of ' + str(secretNumber) + '.')

print('Done.')



