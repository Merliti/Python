"""
     Write a program that takes a number N from the user, then creates a dictionary of keys 1 through N with values that are the squares of the keys.
"""


def dict_of_squares():
    number = int(input("Give me a positive number to square up to: "))
    sqr_dict = {}

    if number > 0:
        i = 1
        while i <= number:
            sqr_dict[i] = i * i
            i += 1

    print(sqr_dict)

dict_of_squares()
