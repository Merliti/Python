# Reverse the order of words in a given sentence.
import string

str_val = "Hello World"
list_val = str_val.split(" ")

print(list_val[::-1])

#Write a program  that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

list1 = [10, 23, 23, 5, 67, 10]
print(set(list1))

#Write a password strength verifier in Python that checks if user password is strong.
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.

password= "1EggPerD@y"
#TESTING
"""print(any(c.isdigit() for c in password))
print(any(c.isupper() for c in password))
print(any(c.islower() for c in password))
print(any(not c.isalnum() for c in password))
print("***********")"""
# END TESTING

# Below did not work
"""
if any(var.isdigit() and var.isupper() and var.islower() and not var.isalnum() for var in password):
    print("***True***")
else:
    print("***False***")"""
#
#Working one but repetitive code
if any(var.isdigit()for var in password) and any(c.isupper() for c in password) and any(b.islower() for b in password) and any(not v.isalnum() for v in password):
    print("***True***")
else:
    print("***False***")

# Write a program to reverse row sort in list of lists

list_id = [[4,1,6], [7,9], [8,9,2,4]]

for x in list_id:
    x.sort(reverse=True)

print(list_id)
print("**************")

# Write a program to pair elements with rear element in matrix row

list_matrix = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
new_list = []

for x in list_matrix:
        for r in x:
            if r != x[-1]:
                v=[r, x[-1]]
                new_list.append(v)

print(new_list)

# Replace each special symbol with # in the following string
# Hint: import string, and use string.punctuation

str1 = "%There &are three( students$ and& 1 trainer!"

for i in str1:
    # checking whether the char is punctuation.
    if i in string.punctuation:
        # Printing the punctuation values
        str1= str1.replace(i, "#")

print(str1)

#Remove all characters for string except integers
str111 = "My mum has a 10 year old dog and 2 fishes"

new_str111 = "".join([x for x in str111 if x.isdigit()])
print(new_str111)

#Remove all empty strings from a list of strings

name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']

filtered_objects = filter(None, name_list)
filtered_name_list = list(filtered_objects)

print(filtered_name_list)