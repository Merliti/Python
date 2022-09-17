"""
    Set:
        - a collection
        - unordered, running(print) will show different order each time
        - unchangeable
        - unindexed, you cannot access then through index
        - created/denoted with {}
        - set do not allow duplicates
"""
myset = {'mangos', 'guavas', 'berries', 'melon'}
print(len(myset))
print('berries' in myset)

"""
    Add items to a set:
        - add <<set>>.add(<item>)
        - update - adds items from a set into another set
            <<set>>.update(<<set2>>)
        -  add any iterable/collection
"""
nuts = {'cashew', 'peanut', 'almond'}
myset.update(nuts)

citrus = ['oranges', 'lemon', 'lime']
myset.update(citrus)

#print(myset)

'''
    Removing element from a set:
        - remove(<<item>>) this generates an error if item doens't exist
        - pop: removes the last item in the set. But you have no idea/control over what is being removed <---- BAD
        - discard- doesn't return error if item isn't found <--- GOOD
        - clear
'''
myset.remove('lime')

"""
Joining of set:
    - union: create a new set with item from the 2 sets.
    Union also removes duplicates if it occures
    
To get common value:
    <<set1>>.intersection_update(<<set2>>)
"""
set1 = {'peanut', 'oranges', 'almonds', 'lime'}
set2 = {'bananas', 'lime', 'pear'}

set3= set1.union((set2))
print(set3)

set1.intersection_update(set2)
print("************************")
print(set1)
print(set2)
print(set3)
print(set3.isdisjoint(set2))



