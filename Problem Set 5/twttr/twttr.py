def main():
    str = input("Input: ")
    print("Output:", shorten(str))
def shorten(str):
    new_str =""
    for i in range(len(str)):
        if(str[i]!="O" and str[i]!="o" and str[i]!="I" and str[i]!="i" and str[i]!="A" and str[i]!="a" and str[i]!="E" and str[i]!="e" and str[i]!="U" and str[i]!="u"):
            new_str += str[i]
    return new_str

if __name__ == "__main__":
    main()
