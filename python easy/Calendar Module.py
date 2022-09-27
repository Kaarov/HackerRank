import calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

a = input().split()
year = int(a[2])
month = int(a[0])
day = int(a[1])

week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(week[calendar.weekday(year, month, day)])

# Done ✅