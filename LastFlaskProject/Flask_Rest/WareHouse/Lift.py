class Lift:
    def __init__(self, y):
        self.available = True
        self.x = 0
        self.y = y
        self.lift = 0
        self.ps = "Empty"
        self.dir = "E"

    def move_North(self):
        self.y = self.y + 1

    def move_South(self):
        self.y = self.y - 1

    def move_East(self):
        self.x = self.x + 1

    def move_West(self):
        self.x = self.x - 1

    def lift_Up(self):
        if (self.lift == 2){
        break;
        }
        self.lift = self.lift + 1



    def start(self):
        pass
    def stop(self):
        pass
    def pause(self):
        pass
