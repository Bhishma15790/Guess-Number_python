import random
from re import X

def guess(x):
    random_number = random.randint(10,x)

    guess = 0
    while guess != random_number:
        guess = int(input(f'guess the number between 10 and{x}:'))

        if guess < random_number:
            print("your guess is too low. 'try again!'")
        elif guess > random_number:
            print("your guess is too high .'Try again!'")

    print(f"Nice! you guess the corrrect number{random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high :
            guess = random.randint(low,high)

        else:
            guess = low

        feedback = input(f"Is {guess} too high(H) too LOW(L) correct(C)").lower()
        if feedback == 'h':
            guess = high-1
        elif feedback == "l" :
            guess = low-1
    
    print(f"computer guess the right number {guess}")









computer_guess(15)
    

