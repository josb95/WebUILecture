max = 2

class Rack :
    def __init__(self ,name ,stuff, quantity, x, y):
        self.name = name
        self.stuff = stuff
        self.quantity = quantity
        self.x = x
        self.y = y
        self.isFull = False
        self.hasTimeStamp = False

    def put(self, stuff):
        if self.quantity >= max:
            if self.quantity == 0:
                self.stuff = stuff
            self.quantity = self.quantity + 1
            if self.quantity == max:
                self.isFull = True
        elif self.isFull == True:
            print("Wrong Access")
        

    def get(self):
        if self.quantity != 0:
            self.quantity = self.quantity - 1
            if self.quantity == 0:
                self.stuff = 'None'
        elif self.quantity == 0:
            print("Wrong Access")

    
