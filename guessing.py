import random as rd

def guess(x):
    random_number = rd.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter a number from 1 and {x}: '))
        if guess > random_number:
            print("Too high, guess again")
        elif guess < random_number:
            print("Too low, guess again")
        else:
            print(f'{guess} is the correct answer')

guess(10)