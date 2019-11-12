class Stock:
    def __init__(self, name, stock):
        self.name = name
        self.quantity = quantity
    
    def add(self):
        self.quantity = quantity + 1

    def minus(self):
        if self.quantity != 0:
            self.quantity = quantity - 1
        else:
            print("Wrong Access")
    
    def set(self, quantity):
        self.quantity = quantity
