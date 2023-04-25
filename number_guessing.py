import random
import time

print('Guess this number between 1 and 1000')

number = random.randint(1, 1000)
guess = 0
count = 0

while guess != number:
    guess = int(input('Your guess: '))
    count += 1
    if guess < number:
        print('Your guess is to low!')
    if guess > number:
        print('Your guess is to high!')
    if guess == number:
        print('Congrats thats the right number with ' + str(count) + ' trys!')
        break

    