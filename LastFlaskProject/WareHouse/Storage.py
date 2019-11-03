import numpy as np;
import networkx as nx;



class Storage:
    def __init__(self, row, col) :
        self.row = row
        self.col = col
        self.g   = nx.grid_2d_graph(row,col)

    def init_graph(self):

      #  self.g.add_node(1);
      #  self.g.add_node(2);
      #  self.g.add_node(3);
      #  self.g.add_nodes_from( [1,2,3,4,5,6] )
      #  for i in range(1,6):
      #      self.g.add_edge(i, i+1)
        pass

    def show(self):
        print(self.MAP)






