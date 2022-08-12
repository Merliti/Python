"""
 - strings in python are arrays
 - the first position is 0 for array_like objects
 """

hello = "Welcome to python"

# print(hello[0])
# print(hello[1])


"""
    looping through a string
    for <<variable_name_for_each_char>> in <<string>>
        statement
    
"""

for cr in hello:
    print(cr)


"""
    length of a string: len(<<string>>
"""
print(len(hello))

"""
    check if a character or phrase exist: in
"""
txt = "Mass Effect"
print("ass" in txt)
print("Eff" not in txt)

"""
    slicing of string: <<string>>[<<start_index>> : <<end_index>>]
    slice from a position to end: <<string>>[<<start_index>>:]
    slice form end to a position: use negative index
"""

"""print(txt[3:7])
print(txt[7:])
print(txt[-1])  # returns a last character in array
print(txt[-4:-1])  # returns a last character in array"""

"""
lower() or casefold() = return to lowercase

"""
print(txt.capitalize())
print(txt.upper())
print(txt.count('t'))