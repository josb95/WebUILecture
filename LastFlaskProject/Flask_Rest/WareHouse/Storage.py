import numpy as np
import networkx as nx
import Rack as R
import Lift as L



class Storage:
    def __init__(self, row, col) :
        self.row = row
        self.col = col
        # self.g   = nx.grid_2d_graph(row,col)
        self.map = np.zeros(row * col).reshape(row, col)
        self.rack1 = R.Rack('A', 'None', 0, 1, 2)
        self.rack2 = R.Rack('B', 'None', 0, 1, 3)
        self.rack3 = R.Rack('C', 'None', 0, 1, 5)
        self.rack4 = R.Rack('D', 'None', 0, 1, 6)
        self.rack5 = R.Rack('E', 'None', 0, 3, 2)
        self.rack6 = R.Rack('F', 'None', 0, 3, 3)
        self.rack7 = R.Rack('G', 'None', 0, 3, 5)
        self.rack8 = R.Rack('H', 'None', 0, 3, 6)
        
        
    def add_Lift(self, liftname, y):
        setattr(self, liftname, L.Lift(y))
        
    def write_TimeStamp(self):
        # 물건 수량이 0이 될 때 타임스탬프를 기록하는 함수
        
        pass

    def update_TimeStamp(self):
        # 일정 주기로 혹은 특정 조건으로 임시로 늘려놓은 물건 수량을 원래대로 되돌려놓는 함수
        
        pass
        
    def received(self):
        # 입고
        
        pass
    
    def requisition(self):
        # 출고
        
        pass
    
    def bad(self):
        # 불량
        
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


#

#


# test part start
s = Storage(9,5)
s.add_Lift('lift1', 0)
print(s.lift1.x)
print(s.lift1.y)
print(s.lift1.available)    
# test part end