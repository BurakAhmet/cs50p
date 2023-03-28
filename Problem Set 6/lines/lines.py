import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

extension = sys.argv[1].split(".")
if len(extension) < 2 or extension[1] != "py":
    sys.exit("Not a Python file")


def main():
    counter = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.isspace() and not line.lstrip().startswith("#"):
                    counter += 1
        print(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
