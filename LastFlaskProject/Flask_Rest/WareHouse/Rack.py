import WareHouse.Stuff as Stu
# import Stuff as Stu
import random as ran
max = 2
ratio_good = 60


class Rack:
    def __init__(self, name, stuff, quantity, col, row):
        self.name = name
        self.stuff = stuff
        self.quantity = quantity
        self.col = col
        self.row = row
        self.isFull = False
        self.stuff_list = list()
        self.stuff_name_list = list()


    def check_Quantity(self):
        self.quantity = len(self.stuff_list)
        if self.quantity >= max:
            self.isFull = True
        else:
            self.isFull = False

    def check_Quantity(self, flag):
        # len 함수로 list 내 개수 확인
        self.quantity = len(self.stuff_list)
        # bool isFull 갱신
        if self.quantity >= max:
            self.isFull = True
            if flag == 0:
                return False
            else:
                return True
        else:
            self.isFull = False
        
        if self.quantity == 0:
            if flag == 0:
                return True
            else:
                return False
        
        return True

    def add_Stuff(self, id, stuffname):
        # randint 를 통한 1% 단위로 랜덤하게 불량 발생
        
        if len(self.stuff_name_list) > 0:
            if stuffname != self.stuff_name_list[0]:
                print("선반에 있는 물건과 넣으려는 물건이 일치하지 않습니다.")
            else:
                if self.check_Quantity(0):
    
                    rand = ran.randint(1, 100)

                    if rand > ratio_good:
                        rand_b = True
                    else:
                        rand_b = False

                    self.stuff_name_list.append(stuffname)
                    setattr(self, id, Stu.Stuff(id, stuffname, rand_b))
                    self.stuff_list.append(getattr(self, id))
                    # 외부에서 사용할 때 id에 대한 자동 증가 카운터 필요
                    if rand_b:
                        print("물건 '{}'에 불량 발생".format(stuffname))

                    self.check_Quantity(self)
                else:
                    print("선반이 꽉찼습니다.")
        else:
            if self.check_Quantity(0):

                rand = ran.randint(1, 100)

                if rand > ratio_good:
                    rand_b = True
                else:
                    rand_b = False
                self.stuff = stuffname
                self.stuff_name_list.append(stuffname)
                setattr(self, id, Stu.Stuff(id, stuffname, rand_b))
                self.stuff_list.append(getattr(self, id))
                # 외부에서 사용할 때 id에 대한 자동 증가 카운터 필요
                if rand_b:
                    print("물건 '{}'에 불량 발생".format(stuffname))
                        
                self.check_Quantity(self)
            else:
                print("선반이 꽉찼습니다.")
        
        
        
    # name을 받고 해당 name과 일치하는 id를 for문을 돌려 찾기
    # for문을 돌려서 객체를 찾은 후 삭제하고 for문 break
    
    def remove_Stuff_byName(self, name):
        for i in self.stuff_list:
            if i.name == name:
                self.remove_Stuff(i.id)
            break
    
    def remove_Stuff(self, id):
        if self.check_Quantity(1):
            self.stuff_name_list.remove(getattr(self, id).name)
            self.stuff_list.remove(getattr(self, id))
            delattr(self, id)
            self.check_Quantity(self)
            
            if self.quantity == 0:
                self.stuff = 'None'
        else:
            print("선반이 비어있습니다.")
            
    
