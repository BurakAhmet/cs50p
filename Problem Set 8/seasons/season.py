from datetime import date
import sys
import inflect
import re


class Date:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not year:
            raise ValueError("Missing year")
        self._year = int(year)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not month:
            raise ValueError("Missing month")
        self._month = int(month)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not day:
            raise ValueError("Missing day")
        self._day = int(day)

    def __str__(self):
        return f"{self._year}-{self._month}-{self._day}"


def main():
    birth_date = input("Date of Birth: ")
    validate(birth_date)
    year, month, day = birth_date.split("-")
    d = Date(year, month, day)
    print(calc(d))


def validate(birth_date):
    if not re.search(r"^([0-9]{4})-((1[0-2])|(0[1-9]))-((0[1-9])|(1[0-9])|(2[0-9])|(3[0-1]))$", birth_date):
        sys.exit("Invalid date")


def calc(d):
    i = inflect.engine()
    birth_date = date(d.year, d.month, d.day)
    current_date = date.today()

    difference = current_date - birth_date
    minutes = difference.days * 24 * 60
    ret = i.number_to_words(minutes, andword="")
    return f"{ret.capitalize()} minutes"


if __name__ == "__main__":
    main()
