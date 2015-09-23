year  = 1899
month = 12
day = 31
week_day = 7
count = 0
count_sun = 0

start = 1901
end = 2000

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while year <= end:

    if week_day == 7:
        week_day = 1
    else:
        week_day += 1

    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        months[1] = 29
    else:
        months[1] = 28

    if day < months[month - 1]:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1


    if year >= start and year <= end:
        count += 1
        if day == 1 and week_day == 7:
            count_sun += 1

print("%d years, %d leap years" % (round(count/365.25), count % 365))
print(count_sun)
