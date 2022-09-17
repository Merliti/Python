"""
    Ask the user for items to be added into two lists.
     To do this, the user first adds to the first list until he enters a zero.
     Then it adds to the second list until it types zero again.
     Create sets out of these two lists.
     Your task is to display the sorted symmetric difference of the sets created from these two lists.
"""
""" POOLIK!!!"""

def words_to_set():
    list1 = []
    list2 = []
    second_round = False
    i = 1

    print("Lets save some words to a list. Write '0' to save list")
    while i == 1:

        word = input("Write the word to add: ")
        word.lower()

        if word != "0" and second_round == False:
            list1.append(word)
            print(f"Appending word to LIST 1 : {word}")
        elif word != "0" and second_round == True:
            print(f"Appending word to LIST 2 : {word}")
            list2.append(word)
        elif word == "0" and second_round == False:
            second_round = True
            print(f"Second round: {second_round}")
        elif word == "0" and second_round == True:
            i = 0
            print(f" Changin i: {i}")

    tuple1 = tuple(list1)
    tuple2 = tuple(list2)

    list_set = set(tuple1)
    list_set_union = set(tuple1)

    list_set.update(tuple2)
    list_set_union.union(tuple2)

    #print(f"Printing LIST 1 : {list1}")
    #print(f"Printing LIST 2 : {list2}")
    print(f"Printing SET  : {list_set}")
    print(f"Printing SET UNION : {list_set_union}")

def sym_difference(set1, set2):
    i = 0
    diff_set= tuple
    if set1[i] == set2[i]:
        print(f"sets are same {set1[i]}")
    else:
        list(diff_set).append(set1[i])




words_to_set()
