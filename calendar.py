from calendar import day_name
month, day, year = map(int,input().split())
print((calendar.day_name[calendar.weekday(year, month, day)]).upper())