def main():
    greeting = input("Greeting: ")
    hello_detector(greeting)

def hello_detector(str):
    str = str.strip()
    if("Hello" in str):
        print("$0")
    elif(str[0] == "H"):
        print("$20")
    else:
        print("$100")
main()
