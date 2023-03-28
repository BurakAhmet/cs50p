import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

after = []
try:
    with open(sys.argv[1]) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            last_name, first_name = row["name"].split(", ")
            after.append({"first": first_name, "last": last_name, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


def main():
    with open(sys.argv[2], "w") as file2:
        writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in after:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()
