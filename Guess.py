import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(
            input(f"Please guess the random number between 1 and {x}: "))
        if guess < random_number:
            print("Please choose something higher")
        elif guess > random_number:
            print("Please choose something lower")

    print("Hooray")


guess(5)
