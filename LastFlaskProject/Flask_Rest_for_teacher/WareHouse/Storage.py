import numpy as np
import time as t
import networkx as nx
import WareHouse.Rack as R
import WareHouse.Lift as L
import WareHouse.Stock as Sto
import WareHouse.Stuff as Stu


class Storage:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.arange(row * col).reshape(row, col)

        self.lift_list = list()
        self.stock_list = list()
        self.rack_list = list()
        self.stuff_list = list()
        
        # self.g   = nx.grid_2d_graph(row,col)
        
    def add_rack(self, rackname, stuffname, stock, col, row):
        setattr(self, rackname, R.Rack(rackname, stuffname, stock, col, row))
        self.rack_list.append(getattr(self, rackname))
        
        # rack1 = R.Rack('A', 'None', 0, 1, 2)
        # rack2 = R.Rack('B', 'None', 0, 1, 3)
        # rack3 = R.Rack('C', 'None', 0, 1, 5)
        # rack4 = R.Rack('D', 'None', 0, 1, 6)
        # rack5 = R.Rack('E', 'None', 0, 3, 2)
        # rack6 = R.Rack('F', 'None', 0, 3, 3)
        # rack7 = R.Rack('G', 'None', 0, 3, 5)
        # rack8 = R.Rack('H', 'None', 0, 3, 6)
        
        
    # 설명용 코드 필드 시작
    # s = Storage(9, 5)
    # s.add_Lift('lift1', 0)
    # s.lift1 = L.Lift(0)
    # 설명용 코드 필드 끝


    def add_Lift(self, liftname, y):
        # Lift를 추가하는 함수
        setattr(self, liftname, L.Lift(y))
        self.lift_list.append(getattr(self, liftname))
        print("Lift name : "+liftname+" added")

    def remove_Lift(self, liftname):
        # Lift 인스턴스 삭제 (객체 소멸자 사용 + list.remove())
        self.lift_list.remove(getattr(self, liftname)) # lift_list list에서 해당 객체 삭제
        delattr(self, liftname) # 객체 소멸
        print("Lift name : "+liftname+" has removed")


    def add_Stock(self, stockname, name, stock):
        # Stock을 추가하는 함수
        # stuffname - 인스턴스 이름, name - 물건이름, stock - 물건 수
        setattr(self, stockname, Sto.Stock(name, stock))
        self.stock_list.append(getattr(self, stockname))
        print("Stock name : " + stockname + " added")

    def remove_Stock(self, stockname):
        # Stock 인스턴스 삭제
        self.stock_list.remove(getattr(self, stockname)) # stock_list list에서 해당 객체 삭제
        delattr(self, stockname) # 객체 소멸
        print("Stock name : " + stockname + " has removed")


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



# # test part start
# s = Storage(9, 5)

# # test map startd
# s.show()
# print(s.map[0][0])
# print(s.map[1][0])
# # test map end

# # list append test start
# s.add_Lift('lift1', 0)
# print(s.lift1.x)
# print(s.lift1.y)
# print(s.lift1.available)
# s.add_Lift('lift2', 1)
# print(s.lift2.x)
# print(s.lift2.y)
# print(s.lift2.available)
# print(s.lift_list)
# s.remove_Lift('lift1')
# print(s.lift_list)
# # print(s.lift1)
# # print(s.lift_list[0])
# # print(s.lift_list[1])
# # list append test start

# # test part end
