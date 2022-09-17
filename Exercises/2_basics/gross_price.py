"""
    Write a function that, based on the given dictionary with purchases as keys and a tuple with price and tax as a value, will calculate the gross amount of all purchases.
     The grocery_list parameter can take the form:
     {"milk": (5.00, 10), "cheese": (4.50, 15), "yogurt": (3, 25)}.
     The first value in a tuple is the net price, the second is the tax (e.g. for 10%
     tax of a given product and its gross price 10, the gross price will be
     was 1.1 * 10). You should add up gross prices for each product
     and return the result.
     It should be assumed that the user will not provide erroneous values (i.e. that the price will never be negative, and the tax will always be included in the set <0; 100>.
"""
shop_items = {
    "milk" : (1, 10),
    "cookies" : (2, 20),
    "bread" : (1.5, 20),
    "bananas" : (0.9, 15),
    "toaster" : (15, 5),
}

def calculate_brutto_prize(grocery_list):
    """Calculates the gross price of all purchases from the grocery_list.

     : param grocery_list: a dictionary, the keys of which are strings representing purchases,
         and tuples with two numbers: the price of the product and its tax.
     : return: sum of all gross values in the list (as a number).

    """
    #while grocery_list:
        #grocery_list[]
    for item in grocery_list:
        grocery_list[item]
        print(item, grocery_list[item])


calculate_brutto_prize(shop_items)