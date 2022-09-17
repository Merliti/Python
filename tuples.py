"""
    Tuples:
        - ordered
        - unchangeable
        - created/denoted with ()
        - allow duplicates
"""
tuple1 = ('oranges',) # put a comma after a tuple with 1 item
print(type(tuple1))

"""
    add item : convert tuple to a list, append  d item and convert back to a tuple
"""

x = list(tuple1)
x.append('lime')
tuple1 = tuple(x)
print(tuple1)

tuple2 = ('lemon',)
tuple1+=tuple2
print(tuple1)
"""
    Unpacking of tuble
        the number of items in your tuple should be equal to the length of the tuple
            * if not, you can use * to unpack the remaining to a list
"""

fruit1, fruit2, fruit3 = tuple1

print(fruit2)

fruit_1, *fruit_2= tuple1

print(fruit_2)
print(fruit_1)