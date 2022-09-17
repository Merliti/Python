"""
    lists are used to store multiple values in a variable
    lists are denoted/created using []
    list are ordered collection of items
    allow duplicates
    changable - add, remove, replace
"""
mylist = ["apple", 'mangos', 'red']

print(type(mylist))
print(mylist[2])
print(mylist[-1])

fruits=["banana", "grapes", "mango"]
mylist.extend(fruits)

print(mylist)

mylist[1] = "yellow"

print(mylist)
"""
    remove items in a list:
        - remove: <<list>>.remove(<<item>>)
        - pop: removes the last item <<list>>.pop()
        - <<list>>.pop(<<index>> : removes item at the position
        - clear: removes all the items in a list, but not the list itself
"""

mylist.pop()
print(mylist)

age = [12, 14, 23, 45, 89, 38, 13]
print(min(age))
print(max(age))
print(sum(age))
print(sum(age) / len(age))

mylist.sort()
age.sort()
print(mylist)
print(age)

"""
    looping through a list
        -for loop
            for <<variable>> in << list >>:
                statement
"""

for var in mylist:
    print(f"I love {var}") # f string
    #print(f"I love" + var)
    #print(f"I love {}".format(var))

range(10) # 0-9
range(5, 10, 2) # 5-9 range(from, to, step)

#for x in range(5, 19, 3):
    #print(x)

for i in range(len(age)):
    print(f"index {i}, value: {age[i]}")

"""
List comprehension: 
    - creates a new list
    - short method of creating a list from an existing list
    - filter and perform operations
    [expression for <<variable_name>> in <<list>> <<optional: condition>>]  **Expression being the thing you want to perform/do with the list
"""
#[print(x) for x in age] not adviced

new_age = [x for x in age if x%2 == 0]
print(new_age)

upp_list = [var.upper() for var in mylist]
print(upp_list)


