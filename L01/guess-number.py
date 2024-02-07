import random

number = random.randint(0, 100)

while 1:
    guess = int(input("please enter an integer:"))

    if guess == number:
        print("u win!")
        break
    elif guess > number:

        print("too large")
    elif guess < number:
        print("too small")
