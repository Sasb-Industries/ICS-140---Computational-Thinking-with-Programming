# Gather in put in seconds from user

print("This Program will convert an amount of seconds you type in, into weeks, days, hours, minutes, and seconds.")
inputTime = int(input("Please enter a number of seconds you would like to get converted : "))

# Process seconds into appropriate time intervals
weekSeconds = 604800 # number of seconds in a week
daySeconds = 86400 # Number of seconds in a day
hourSeconds = 3600 # Number of seconds in an hour
minuteSeconds = 60 # Number of seconds in a minute

week = int(inputTime/weekSeconds)
weekRemainder = inputTime % weekSeconds

day = int(weekRemainder/daySeconds)
dayRemainder = weekRemainder % daySeconds

hour = int(dayRemainder/hourSeconds)
hourRemainder = dayRemainder % hourSeconds

minute = int(hourRemainder/minuteSeconds)
minuteRemainder = hourRemainder % minuteSeconds

second = minuteRemainder

#display output
print(f"{week} week(s), {day} days(s), {hour} hour(s), {minute} minute(s), {second} second(s)")
# print(f"week remainder: {weekRemainder}")
# print(f"days remainder: {dayRemainder}")
# print(f"hours reaminder: {hourRemainder}")
# print(f"minutes reaminder: {minuteRemainder}")