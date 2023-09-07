def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_input, month_input):
    month_days = [31, 28, 31, 30,]

    if month_input == 2 and is_leap(year_input) is True:
        selection = month_days[1] = 29
    elif month_input == 2:
        selection = month_days[1]
    elif month_input == 4 or month_input == 6 or month_input == 9 or month_input == 11:
        selection = month_days[3]
    else:
        selection = month_days[0]

    return selection

    # 🚨 Do NOT change any of the code below


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
