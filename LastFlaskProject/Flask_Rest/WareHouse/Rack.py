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
            self.quantity = self.quantity + 1
            if self.quantity == max:
                self.isFull = True
        elif self.quantity == 0:
            self.stuff = stuff

    def get(self):
        if self.quantity != 0:
            self.quantity = self.quantity - 1
            if self.quantity == 0:
                self.stuff = 'None'
                write_TimeStamp()
        elif self.quantity == 0:
            print("Wrong Access")

    def write_TimeStamp(self):
        # 물건 수량이 0이 될 때 타임스탬프를 기록하는 함수
        pass

    def update_TimeStamp(self):
        # 일정 주기로 혹은 특정 조건으로 임시로 늘려놓은 물건 수량을 원래대로 되돌려놓는 함수
        pass
