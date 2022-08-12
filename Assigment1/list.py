# Create a new string made of the middle three characters of an input string

input = "JhonDipPeta"

print(input[int(len(input)/2 - 1): int(len(input)/2 + 2)])

#Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Aunt"
s2 = "Sister"
s3 = (s2[0: int(len(s2)/2)] + s1 + s2[int(len(s2)/2): ])

print(s3)

#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

s1 = "America"
s2 = "Japan"

s3 = s1[0] + s2[0] + s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)] + s1[-1] + s2[-1]
print(s3)

#Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.

s1 = "Yn"
s2 = "PYnative"
print(s1 in s2)

s3 = "Ynf"
s4 = "PYnative"
print(s3 in s4)

# Write a program to split a given string on hyphens and display first and last substring.

str1 = "Emma-is-a-data-scientist"
resultEmma = str1.split("-")[0] + ", " + str1.split("-")[-1]
print(resultEmma)

#Reverse a given string
#Write a program to find the last position of a substring “Emma” in a given string.

str2 = "Emma is a data scientist who knows Python. Emma works at google."
print(str2[::-1])
h = str2.find("Emma", str2.find("Emma") + 1, len(str2))
print(f"Last occurrance of Emma starts at index {h}")