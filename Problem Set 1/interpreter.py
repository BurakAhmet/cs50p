def main():
    expression = input("Expression: ")
    interpreter(expression)
def interpreter(exp):
    x, y, z = exp.split(" ")
    x = float(x)
    z = float(z)
    if(y=="+"):
        print(x+z)
    elif(y=="-"):
        print(x-z)
    elif(y=="*"):
        print(x*z)
    else:
        print(x/z)
main()
