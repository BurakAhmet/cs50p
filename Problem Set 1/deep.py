def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if(is_meaning_of_life(x)):
        print("Yes")
    else:
        print("No")
def is_meaning_of_life(str):
    str = str.casefold().strip()
    if(str == "42" or str == "forty two" or str == "forty-two"):
        return True
    return False
main()
