"""
    Write a function whose task is to double each character in the string given as an input parameter.
     For example, the value returned from the produce_double_sings function for "Python" should be "PPyytthhoonn".
     Each letter should be doubled.
     We only consider single-word subtitles.
"""


def produce_double_signs(string):
    """Creates a new string from the given one, doubling each character.

     :param string: string where characters should be doubled
     :return: new string with duplicate characters.

    """
    i = 0
    double_string = ""
    while i < len(string):
        double_string += string[i] + string[i]
        i += 1

    print(f"Double: {double_string}")


produce_double_signs("Python")
