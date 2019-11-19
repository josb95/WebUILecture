import numpy as np
import time as t
import networkx as nx
# 외부 실행용
import WareHouse.Rack as R
import WareHouse.Lift as L
import WareHouse.Stock as Sto

# 내부 실행용
# import Rack as R
# import Lift as L
# import Stock as Sto

counter_list = list()
stockname_list = list()
    

class Storage:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.arange(row * col).reshape(row, col)

        self.lift_list = list()
        self.stock_list = list()
        self.rack_list = list()
        self.stuff_name_list_all = set()  # 수량 계산 함수에 의해 list로 바뀜
        self.stock_dict = dict()
        self.stock_setting_dict = dict()

    # 인스턴스 추가, 제거 함수 =================================================

    def add_rack(self, rackname, stuffname, stock, col, row):
        # Rack을 추가하는 함수 - 제거 불필요
        setattr(self, rackname, R.Rack(rackname, stuffname, stock, col, row))
        self.rack_list.append(getattr(self, rackname))

    def add_Lift(self, liftname, y):
        # Lift를 추가하는 함수
        setattr(self, liftname, L.Lift(y))
        self.lift_list.append(getattr(self, liftname))
        print("Lift name : " + liftname + " added")

    def remove_Lift(self, liftname):
        # Lift 인스턴스 삭제 (객체 소멸자 사용 + list.remove())
        # lift_list list에서 해당 객체 삭제
        self.lift_list.remove(getattr(self, liftname))
        delattr(self, liftname)  # 객체 소멸
        print("Lift name : " + liftname + " has removed")

    def add_Stock(self, stockname, name, stock):
        # Stock을 추가하는 함수
        # stuffname - 인스턴스 이름, name - 물건이름, stock - 물건 수
        setattr(self, stockname, Sto.Stock(name, stock))
        self.stock_list.append(getattr(self, stockname))
        print("Stock name : " + stockname + " added")

    def remove_Stock(self, stockname):
        # Stock 인스턴스 삭제
        # stock_list list에서 해당 객체 삭제
        self.stock_list.remove(getattr(self, stockname))
        delattr(self, stockname)  # 객체 소멸
        print("Stock name : " + stockname + " has removed")

    # =========================================================================

    def calculate_Stock(self):
        # 재고 수량 계산
        counter_list = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in self.rack_list:
            for j in i.stuff_name_list:
                self.stuff_name_list_all.add(j)

        # Set을 정렬 후 List 화
        self.stuff_name_list_all = sorted(self.stuff_name_list_all)

        for i in self.rack_list:
            for j in i.stuff_list:
                for k in range(len(self.stuff_name_list_all)):
                    if j.name == self.stuff_name_list_all[k]:
                        counter_list[k] = counter_list[k] + 1

        self.stock_dict = dict(zip(self.stuff_name_list_all, counter_list))

    def update_Stock(self):
        del self.stock_list
        self.stock_list = list()
        stockname_list = ['Stock_A', 'Stock_B', 'Stock_C',
                          'Stock_D', 'Stock_E', 'Stock_F', 'Stock_G', 'Stock_H']
        cnt = 0
        for i in self.stock_dict:
            key = i
            value = self.stock_dict[key]
            self.add_Stock(stockname_list[cnt], key, value)
            cnt = cnt + 1

    # =========================================================================

    def insert_Setting_Stock(self, key, value):
        self.stock_setting_dict[key] = int(value)
        
    def update_Setting_Stock(self, key, value):
        self.stock_setting_dict[key] = int(value)
        
    def delete_Setting_Stock(self, key):
        del self.stock_setting_dict[key]

    # =========================================================================

    def received(self):
        # 입고

        pass

    def requisition(self):
        # 출고

        pass

    def bad(self):
        # 불량 - 물건 하나하나를 객체로 다루지 않아 삭제 예정
        # => 물건 하나하나 모두 객체화 예정
        pass










    def write_TimeStamp(self):
        # 물건 수량이 0이 될 때 타임스탬프를 기록하는 함수

        pass



    # 보류 기능 시작 =============================================================

    # def update_TimeStamp(self):
    #     # 일정 주기로 혹은 특정 조건으로 임시로 늘려놓은 물건 수량을 원래대로 되돌려놓는 함수

    #     pass

    # def from_StrtoTimestamp(self):
    #     # Str -> Timestamp 형 변환

    #     pass

    # def from_TimestamptoStr(self):
    #     # Timestamp -> Str 형 변환

    #     pass
    
    # 보류 기능 끝 =============================================================


    def show(self):
        print(self.map)


# test part start
# s = Storage(9, 5)
# s.Rack_A
