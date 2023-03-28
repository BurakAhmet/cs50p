import sys
from pyfiglet import Figlet


def main():
    if len(sys.argv) > 3 or len(sys.argv) == 2 or sys.argv[1] != "-f":
        sys.exit("Invalid usage")
    figlet = Figlet()
    data = input("Input: ")
    if len(sys.argv) == 3:
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit("Invalid usage")
    print(figlet.renderText(data))

if __name__ == "__main__":
    main()
