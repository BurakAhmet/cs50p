def main():

    x = get_date()
    date_printer(x)


def get_date():
    while True:
        x = input("Date: ")
        if x.count("/") > 0:
            if x[0].isalpha():
                continue
            index_of_slash1 = x.find("/")
            month = int(x[:index_of_slash1])
            day_str = x[index_of_slash1+1:len(x)]
            index_of_slash2 = day_str.find("/")
            day = int(day_str[:index_of_slash2])
            if month > 12 or day > 31:
                continue
        elif not x[0].isalpha() or x.count(",") == 0:
            continue
        else:
            index_of_comma = x.find(",")
            index_of_blank = x.find(" ")
            day = int(x[index_of_blank + 1:index_of_comma])
            month = x[:index_of_blank]
            months = {
                "January": 1,
                "February": 2,
                "March": 3,
                "April": 4,
                "May": 5,
                "June": 6,
                "July": 7,
                "August": 8,
                "September": 9,
                "October": 10,
                "November": 11,
                "December": 12
            }
            if months.get(month) > 12 or day > 31:
                continue
        return x


def date_printer(date):
    if date.count("/") > 0:
        index_of_slash1 = date.find("/")
        month = int(date[:index_of_slash1])
        day_str = date[index_of_slash1 + 1:]
        index_of_slash2 = day_str.find("/")
        day = int(day_str[:index_of_slash2])
        year = int(day_str[index_of_slash2 + 1:])

        print(f"{year:04}-{month:02}-{day:02}")
    else:
        months = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        index_of_comma = date.find(",")
        index_of_blank = date.find(" ")
        year = int(date[index_of_comma+2:])
        day = int(date[index_of_blank+1:index_of_comma])
        month = date[:index_of_blank]
        print(f"{year:04}-{months.get(month):02}-{day:02}")


main()
