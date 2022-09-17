"""
    Write a program that displays
     the smallest and largest item in a list, and will reverse it.
"""
list1 = [4, 0, 50, 100]

def max_min_list(list):
    print(max(list))
    print(min(list))
    revers = list[::-1]
    print(revers)

max_min_list(list1)