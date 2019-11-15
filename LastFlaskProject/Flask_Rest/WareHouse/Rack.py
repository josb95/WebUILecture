# import WareHouse.Stuff as Stu
import Stuff as Stu
import random as ran
max = 2
ratio_bad = 99


class Rack:
    def __init__(self, name, stuff, quantity, col, row):
        self.name = name
        self.stuff = stuff
        self.quantity = quantity
        self.col = col
        self.row = row
        self.isFull = False
        self.hasTimeStamp = False
        self.stuff_list = list()
        self.stuff_name_list = list()


    def check_Quantity(self):
        # len 함수로 list 내 개수 확인
        self.quantity = len(self.stuff_list)
        # bool isFull 갱신
        if self.quantity >= max:
            self.isFull = True
        else:
            self.isFull = False

    def add_Stuff(self, id, stuffname):
        # randint 를 통한 1% 단위로 랜덤하게 불량 발생
        rand = ran.randint(1, 100)
        if rand > ratio_bad:
            rand_b = False
        else:
            rand_b = True

        self.stuff_name_list.append(stuffname)
        setattr(self, id, Stu.Stuff(id, stuffname, rand_b))
        self.stuff_list.append(getattr(self, id))
        # 외부에서 사용할 때 id에 대한 자동 증가 카운터 필요
        self.check_Quantity()

    def remove_Stuff(self, id):
        self.stuff_name_list.remove(getattr(self, id).name)
        self.stuff_list.remove(getattr(self, id))
        delattr(self, id)
        self.check_Quantity()

