#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py
Author: "David Brand"
Semester: "Summer 2026"

The python code in this file (assignment1.py) is original work written by
"David Brand". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys


def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3,
              7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}

    if month < 3:
        year -= 1

    num = (year + year // 4 - year // 100 +
           year // 400 + offset[month] + date) % 7

    return days[num]


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"

    # A year divisible by 400 is a leap year
    if year % 400 == 0:
        return True

    # A year divisible by 100 but not 400 is not a leap year
    if year % 100 == 0:
        return False

    # A year divisible by 4 is a leap year
    if year % 4 == 0:
        return True

    # Otherwise it is not a leap year
    return False


def mon_max(month: int, year: int) -> int:
    "returns the maximum day for a given month. Includes leap year check"

    # February changes depending on whether it is a leap year
    if month == 2:
        if leap_year(year):
            return 29
        return 28

    # Maximum days for all other months
    month_days = {
        1: 31,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_days[month]


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''

    # Split the date string into year, month, and day
    str_year, str_month, str_day = date.split('-')

    # Convert the string values to integers
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # Move forward one day
    tmp_day = day + 1

    # Check if the day exceeds the maximum day for the month
    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    # Check if the month exceeds December
    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month

    # Format the next date as YYYY-MM-DD
    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")


def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    parts = date.split('-')
    if len(parts) != 3:
        return False

    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True


def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    current = start_date
    weekends = 0

    while current <= stop_date:
        year, month, day = current.split('-')
        weekday = day_of_week(int(year), int(month), int(day))
        if weekday == 'sat' or weekday == 'sun':
            weekends += 1
        current = after(current)

    return weekends


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        sys.exit()

    date1 = sys.argv[1]
    date2 = sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()
        sys.exit()

    start_date, stop_date = sorted([date1, date2])
    weekends = day_count(start_date, stop_date)

    print(f"The period between {start_date} and {stop_date} includes {weekends} weekend days.")

