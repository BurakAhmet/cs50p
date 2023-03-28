def main():
    camel = input("camelCase: ")
    print("snake_case:",camel_to_snake(camel))
def camel_to_snake(str):
    snaked=""
    for i in range(len(str)):
        if(str[i].isupper()):
            snaked += "_"
            snaked += str[i].lower()
        else:
            snaked += str[i]
    return snaked
main()
