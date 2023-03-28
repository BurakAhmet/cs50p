from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

extensions = ["png", "jpg", "jpeg"]

input_format = sys.argv[1].split(".")
input_extension = input_format[1]

output_format = sys.argv[2].split(".")
output_extension = output_format[1]

if input_extension not in extensions or output_extension not in extensions:
    sys.exit("Invalid input")

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")


def main():
    try:
        photo = Image.open(sys.argv[1])
    except:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    fit = ImageOps.fit(photo, size)
    fit.paste(shirt, shirt)
    fit.save(sys.argv[2])

if __name__ == "__main__":
    main()
