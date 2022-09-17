"""
    Write a program that reads a text file and then prints it with numbered lines.
"""
import os

if os.path.exists("text.txt"):
    f = open("text.txt")
    list1 = f.readlines()
    i = 1
    for var in list1:
        print(f"{i} {list1[i-1]}")
        i+=1
    f.close()