class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    # 정량적 add minus 삭제
    
    def add(self):
        self.quantity = quantity + 1

    def minus(self):
        if self.quantity != 0:
            self.quantity = quantity - 1
        else:
            print("Wrong Access")
    
    def set(self, quantity):
        self.quantity = quantity
        
    def set(self, name, quantity):
        self.name = name
        self.quantity = quantity