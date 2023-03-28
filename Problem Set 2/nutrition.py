def main():
    fruit = input("Item: ")
    matcher(fruit)


def matcher(s):
    s = s.title()
    match s:
        case "Apple":
            print("130 Calories")
        case "Avocado":
            print("50 Calories")
        case "Banana":
            print("110 Calories")
        case "Cantaloupe":
            print("50 Calories")
        case "Grapefruit":
            print("60 Calories")
        case "Grapes":
            print("90 Calories")
        case "Honeydew Melon":
            print("50 Calories")
        case "Kiwifruit":
            print("90 Calories")
        case "Lemon":
            print("15 Calories")
        case "Lime":
            print("20  Calories")
        case "Nectarine":
            print("60 Calories")
        case "Orange":
            print("80 Calories")
        case "Peach":
            print("60 Calories")
        case "Pear":
            print("100 Calories")
        case "Pineapple":
            print("50 Calories")
        case "Plums":
            print("70 Calories")
        case "Strawberries":
            print("50 Calories")
        case "Sweet Cherries":
            print("100 Calories")
        case "Tangerine":
            print("50 Calories")
        case "Watermelon":
            print("80 Calories")


main()
