import random

print('Hello, what is your name?')
name = input()

print('Well, '+ name + ', I am thinking of a number tween 1 to 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, '+ name + ' ! you guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thing of was ' + str(secretNumber))