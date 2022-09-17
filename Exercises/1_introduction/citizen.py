"""
    Write a Citizen class that implements the __init__ method, taking two arguments: first name and last name.
     Create an object of this class, then display the citizen's first and last name.

     Add the set_nationality class method to the Citizen class (and with it the nationality class field with the selected default value).
     Call this method. Create a second class object and see what the nationality field will be in both objects.

     Additionally, you can try adding the total_number_of_citizens class attribute which is a number.
     Increase it each time a new citizen is created.
"""


class Citizen:
    counter = 0

    def __init__(self, fname, lname):
        self.fname = fname,
        self.lname = lname,
        self.nationality = None
        Citizen.counter += 1



    def set_nationality(self, nat = "Unknown"):
        self.nationality = nat

shep = Citizen("Jane", "Shepard")
garrus = Citizen("Carrus", "Vakarien")
Grunt = Citizen("Grunt", "Normandy")
shep.set_nationality("English")
garrus.set_nationality()


print(Citizen.counter)
print(shep.nationality)
print(garrus.nationality)