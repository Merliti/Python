"""
    Create a Notebook class that will contain the fields: manufacturer, net price and RAM memory.
     Add methods to calculate the gross price (+ 20% VAT) and increase the amount of RAM.
"""


class Notebook:
    def __init__(self, manufact, net_price, ram: int):
        self.manufacturer = manufact
        self.net_price: float = net_price
        self.ram: int = ram

    def calc_price(self):
        return self.net_price + (self.net_price * 0.2)

    def inc_ram(self, added_ram: int):
        print(f"Increasing ram from {self.ram} to {self.ram + added_ram}")
        return self.ram + added_ram


note1 = Notebook("Asus", 1200, 4)

print(note1.net_price)
print(note1.calc_price())
print(note1.inc_ram(4))

