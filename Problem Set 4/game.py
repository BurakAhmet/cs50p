import random as random
import sys

def main():
    level = get_valid("Level: ")
    answer = random.randint(1, level)
    guess = get_valid("Guess: ")
    while guess != answer:
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        guess = get_valid("Guess: ")
    print("Just right!")
    sys.exit()


def get_valid(prompt):
    data = 0
    while data < 1:
        try:
            data = int(input(prompt))
        except ValueError:
            continue
    return data


main()
