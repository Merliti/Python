# Task 7: Write a function that will return the 5 most common words from
# Rummo work.
import os

if os.path.exists("poem.txt"):
    f = open("poem.txt")
    word_list = f.read().lower().split()
    # print(word_list)
    word_dict = {}

    for item in word_list:
        if item in word_dict:
            word_dict[item] += 1
        else:
            word_dict[item] = 1

    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    var = 0
    for i in sorted_dict:
        if var <= 5:
            print(i[0], i[1])
            var += 1

    f.close()

# Task 8
"""Create a Rectangle class whose attributes will be the height and width of
the figure. Implement methods to measure the perimeter and area of a
rectangle.
Then create a Square class, remembering that every square is a
rectangle, but not every rectangle is a square."""


class Rectangle:
    def __init__(self, width, height):
        self.width = width,
        self.height = height
        self.isSquare = False

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, width, height):
        if width == height:
            self.width = width
            self.height = width
            self.isSquare = True


rect = Rectangle(4, 6)
sqr = Square(2, 3)
print(sqr.perimeter())
