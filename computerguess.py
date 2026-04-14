import random as rd

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = rd.randint(low, high)
        feedback = input(f'is {guess} too high(H), low(L) or correct(C)').lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'c':
            print(f'{guess}, is the correct answer ')
        
computer_guess(1800)