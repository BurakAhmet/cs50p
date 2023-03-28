def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or 6 < len(s) or s[0].isnumeric() or s[1].isnumeric():
        return False
    elif s.isalpha():
        return True
    i = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            break
    for j in range(i, len(s)):
        if s[i] == "0" or s[j].isnumeric() == False:
            return False
    return True


if __name__ == "__main__":
    main()
