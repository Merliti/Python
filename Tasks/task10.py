total = 0
print("starting...")
def return_a_number():

    def adding(number):
        print("adding...")
        global total
        total = total + number
        return total

    number = int(input("Type your number: "))
    if number == "exit":
        print("Bye")
    else:
        try:
            print(f"your current total: {adding(number)}")
            return_a_number()
        except:
            print("Please insert a NUMBER!")
            return_a_number()


return_a_number()
