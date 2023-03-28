import inflect

def main():
    str = inflect.engine()
    arr = []
    try:
        while True:
            name = input("Name: ")
            arr += [name]
    except EOFError:
        pass
    print("Adieu, adieu, to", str.join(arr))
main()
