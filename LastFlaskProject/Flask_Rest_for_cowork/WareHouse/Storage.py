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

    def initializing_Stock(self):
        pass

    def update_Stock(self):
        pass

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

    def select_Lift(self):
        # (옮길 물건에서 가장 가까운) 리프트 선택
        pass

    def calculate_Route(self):
        # 경로계산

        pass

    def send_NextNode(self):
        # 다음 노드 전송

        pass

    def send_StuffStatus(self):
        # 물건 정보 전송

        pass

    def write_TimeStamp(self):
        # 물건 수량이 0이 될 때 타임스탬프를 기록하는 함수

        pass

    def update_TimeStamp(self):
        # 일정 주기로 혹은 특정 조건으로 임시로 늘려놓은 물건 수량을 원래대로 되돌려놓는 함수

        pass

    def from_StrtoTimestamp(self):
        # Str -> Timestamp 형 변환

        pass

    def from_TimestamptoStr(self):
        # Timestamp -> Str 형 변환

        pass

    def init_graph(self):

      #  self.g.add_node(1);
      #  self.g.add_node(2);
      #  self.g.add_node(3);
      #  self.g.add_nodes_from( [1,2,3,4,5,6] )
      #  for i in range(1,6):
      #      self.g.add_edge(i, i+1)
        pass

    def show(self):
        print(self.map)


# test part start
# s = Storage(9, 5)
# s.Rack_A
