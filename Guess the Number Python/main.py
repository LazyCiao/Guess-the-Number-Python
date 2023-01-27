import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        if guess < random_number:
            print('Your guess is too low, try again.')
        elif guess > random_number:
            print('Your guess is too high, try again.')

    print('Yay! You got the right number!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess +1

    print(f'Yay! The computer is a genius')

guess(10)
