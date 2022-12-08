DAYS_IN_MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]

def main():
    print("This program will tell you what day of the year your input is.")
    month = int(input("Please enter the month (1 - 12) : "))
    while month < 1 or month > 12:
        month = int(input("That is not a valid input. Please enter a month (1 - 12) : "))
    day = int(input("Please enter a day for that month : "))
    valid = is_date_valid(month, day)
    while valid == False:
        day = int(input("Invalid Day. Please enter a day for that month : "))
        valid = is_date_valid(month, day)
    day_count = get_day_count(month, day)
    print(f"{month}/{day} is day number {day_count} in the year 2023")



def is_date_valid(month, day):
    if day > 0 and day <= DAYS_IN_MONTHS[month + 1]:
        return True
    else:
        return False

def get_day_count(month, day):
    number_of_days = day
    for i in range(month - 1):
        number_of_days += DAYS_IN_MONTHS[i]
    return number_of_days

main()