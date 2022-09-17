# Reverse list

info = ['karl', '100', 'Red', 'Mangos']
info.reverse()

print(info)

# Add two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [x+y for x, y in zip(list1, list2)]
print(result)

# Find second largest number in given list

list1 = [10, 20, 4]
list1.sort()
list1_nr = list1[-2]
print(list1_nr)

list2 = [70, 11, 20, 4, 100]
list2.sort()
list2_nr = list2[-2]
print(list2_nr)

#Find 20, replace with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]

list1.insert(list2.index(20), 200)

print(list1)

#Count the occurrences of x in given list
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print(lst.count(x))

lst2 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 16
print(lst2.count(x))

#Remove all occurrences of 20. Use list comprehension

list20 = [5, 20, 15, 20, 25, 50, 20]

removed20 = [x for x in list20 if x != 20]
print(removed20)

# Return the middle value of a list. If there are 2 middle values, return the second

names = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
print(names[int(len(names)/2)])

age = [10, 3, 45, 67, 89.0, 45]
print(age[int(len(age)/2)])


