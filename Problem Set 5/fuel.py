def main():
    x = convert("Fraction: ")
    x = gauge(x)
    if x < 10:
        print("E")
    elif x > 90:
        print("F")
    else:
        print(f"{x}%")

def convert(prompt):
    while True:
        x = input("Fraction: ")
        if x.count("/") > 1 or x.count("/") == 0:
            continue
        index_of_slash = x.find("/")
        try:
            int1 = int(x[:index_of_slash])
            int2 = int(x[index_of_slash+1:])
            if int1 > int2:
                continue
            x = int1 / int2
        except ValueError or ZeroDivisionError:
            continue
        return x


def gauge(fraction):
    fraction = int(round(fraction * 100))
    return fraction

if __name__ == "__main__":
    main()
