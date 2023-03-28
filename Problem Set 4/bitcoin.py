import requests
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = request.json()
    worth = response["bpi"]["USD"]["rate_float"] * value
    print(f"${worth:,.4f}")


if __name__ == "__main__":
    main()
