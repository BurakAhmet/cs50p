def main():
    greeting = input("Greeting: ")
    value(greeting)

def value(str):
    str = str.strip()
    if("Hello" in str):
        print("$0")
    elif(str[0] == "H"):
        print("$20")
    else:
        print("$100")
if __name__ == "__main__":
    main()
