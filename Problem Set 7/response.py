import validators


def main():
    mail = input("What's your email address? ")
    if validators.email(mail):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
