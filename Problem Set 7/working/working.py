import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pm_to_24 = {
        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
        "12": "12"
    }
    if hours := re.search(r"((^[1-9]|1[0-2]):?((0[0-9])?|([0-5][0-9])?) (AM|PM)) "
                          r"to (([1-9]|1[0-2]):?((0[0-9])?|([0-5][0-9])?) (AM|PM))$", s):
        converted_hour = ""
        hour1 = hours.groups()[0]
        hour1_hour = hours.groups()[1]
        hour1_minutes = hours.groups()[2]
        if hour1_hour == "12" and "AM" in hour1:
            converted_hour += "00"
        elif "PM" in hour1:
            converted_hour += pm_to_24.get(hour1_hour)
        else:
            if len(hour1_hour) == 1:
                converted_hour += "0" + hour1_hour
            else:
                converted_hour += hour1_hour
        if hour1_minutes:
            converted_hour += ":" + hour1_minutes + " to "
        else:
            converted_hour += ":00 to "

        hour2 = hours.groups()[6]
        hour2_hour = hours.groups()[7]
        hour2_minutes = hours.groups()[8]
        if hour2_hour == "12" and "AM" in hour2:
            converted_hour += "00"
        elif "PM" in hour2:
            converted_hour += pm_to_24.get(hour2_hour)
        else:
            if len(hour2_hour) == 1:
                converted_hour += "0" + hour2_hour
            else:
                converted_hour += hour2_hour
        if hour2_minutes:
            converted_hour += ":" + hour2_minutes
        else:
            converted_hour += ":00"
        return converted_hour
    else:
        raise ValueError


if __name__ == "__main__":
    main()

