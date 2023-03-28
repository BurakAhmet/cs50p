import random


def main():
    level = get_level()
    score = get_score(level)
    print("Score:", score)


def get_score(level):
    score = 0
    for _ in range(10):
        if get_answer(level):
            score += 1
    return score


def get_answer(level):
    x, y = generate_integer(level)
    remainder = 3
    while remainder > 0:
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            remainder -= 1
            print("EEE")
            continue
        if answer != x + y:
            print("EEE")
            remainder -= 1
        else:
            return True
    print(f"{x} + {y} = {x + y}")


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 1 <= lvl <= 3:
                return lvl
        except ValueError:
            continue


def generate_integer(level):
    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    return x, y


if __name__ == "__main__":
    main()
