"""
    Write a program that asks the user to enter the year
     and then checks if the year is a leap year.

     A year is leap when it divides by 400 or when it divides
     by 4, but is not divisible by 100.
"""

def is_a_leap_year():
    year = int(input("Write a year to check:"))
    if year % 4 == 0 or year % 400 ==0 and year % 100 != 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")

is_a_leap_year()