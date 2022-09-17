# sequence of numbers to text

def num_to_text():
    numbers = {"1": "one",
               "2": "two",
               "3": "three",
               "4": "four",
               "5": "five",
               "6": "six",
               "7": "seven",
               "8": "eight",
               "9": "nine",
               "0": "zero",
               }
    number = input("Number: ")
    result = ""
    for x in number:
        result += numbers[x] + " "
    print(result)


# num_to_text()

# From list of integers return smallest number

list1 = [41, 13, 56, 7, 12, 3, 6, 85]


def return_smallest_num(list):
    smallest = 100
    place = 0
    for inx, x in enumerate(list):

        if x < smallest:
            smallest = x
            place = inx

    print(f"{smallest} {place}")


return_smallest_num(list1)


# create a function that checks that the number given is prime. Return logical value

def check_if_prime(number):
    if number % 2 == 0:
        print(False)
    else:
        print(True)


check_if_prime(6)
check_if_prime(147)


def check_if_pali(word):
    word = word.lower()
    rev_word = word[::-1]
    if word == rev_word:
        print(True)

    else:
        print(False)
        print(f"{word} is not pali to {rev_word}")


check_if_pali("madam")


def count_upper_lower(sentence):
    upper_letterce = 0
    lower_letterce = 0

    for x in sentence:
        if x.isupper():
            upper_letterce += 1

        elif x.islower():
            lower_letterce += 1
    print(f"Upper> {upper_letterce}: lower: {lower_letterce}")


count_upper_lower("The quick Brown Fox")


def find_first_string(first, second):
    result=""
    for x in first:
        if x in second:
            result+= x
    print(result)

find_first_string("Hello", "vufigsaHudesklcvlso")

list3 = [23, 45, 3, 9.4, -9999, 87.4, 92 ,2]
idx= 0
sum=0

print(len(list3))

while idx < len(list3):
    sum+=list3[idx]
    idx+=1

    if list3[idx] == -9999:
        break
print(f"sum: {sum}")