class Laptop:

    def __init__(self, name, price, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, customer):
        customer.money -= laptop.price
        self.stock -= 1

class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money


customer = Customer('alex', 200000)
laptop = Laptop('Galaxy_book3', 20000)

laptop.sell(customer)
print(customer.money)