class Lift:
    def __init__(self, y):
        self.available = True
        self.x = 0
        self.y = y
        self.lift_height = 0
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

    def move_Forward(self):
        if self.dir == 'N':
            self.move_North()
        elif self.dir == 'W':
            self.move_West()
        elif self.dir == 'S':
            self.move_South()
        elif self.dir == 'E':
            self.move_East()

    def move_Backward(self):
        if self.dir == 'N':
            self.move_South()
        elif self.dir == 'W':
            self.move_East()
        elif self.dir == 'S':
            self.move_North()
        elif self.dir == 'E':
            self.move_West()

    def turn_Left(self):
        if self.dir == 'N':
            self.dir = 'W'
        elif self.dir == 'W':
            self.dir = 'S'
        elif self.dir == 'S':
            self.dir = 'E'
        elif self.dir == 'E':
            self.dir = 'N'

    def turn_Right(self):
        if self.dir == 'N':
            self.dir = 'E'
        elif self.dir == 'E':
            self.dir = 'S'
        elif self.dir == 'S':
            self.dir = 'W'
        elif self.dir == 'W':
            self.dir = 'N'

    def lift_Up(self):
        if self.lift_height == 2:
            return
        self.lift_height = self.lift_height + 1

    def lift_Down(self):
        if self.lift_height == 0:
            return
        self.lift_height = self.lift_height - 1
        
    def pick_Stuff(self, stuffname):
        self.ps = stuffname
