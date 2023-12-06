import copy
import numpy as np

class Q_table:
    def __init__(self) -> None:
        self.table = np.zeros((7, 10), dtype=int)
        self.start = (3,0)
        self.destination = (3,7)
        self.agent = self.start
        self.wind = [0,0,0,0,0,0,0,0,0,0] 

    def set_wind(self, array):
        self.wind = array
        for j in range(10):
            if array[j] != 0:
                for i in range(7):
                    self.table[i, j] = array[j]

    def set_start(self, tuple):
        self.start = tuple

    def set_destination(self, tuple):
        self.destination = tuple

    def __str__(self) -> str:
        prt = ""
        for i in range(7):
            for j in range(10):
                if (i, j) == self.agent:
                    prt += "S "
                elif (i, j) == self.destination:
                    prt += "G "
                else:
                    prt += str(self.table[i, j]) + " "
            prt += '\n'
        return prt
    
class Agent:
    def __init__(self) -> None:
        self.enviorment = Q_table()
        self.enviorment.set_wind([0,0,0,1,1,1,2,2,1,0])
        self.position = self.enviorment.start
        self.path = []
        self.lrn_rate = 0.9
        self.eps = 0.001


    def posible_action(self, position):
        movment_pos = []
        if self.enviorment.table[(position)] == 0:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for d in directions:
                (a, b) = (self.position[0] + d[0], self.position[1] + d[1])
                if a<=6 and a>=0 and b<=9 and b>=0:
                    movment_pos.append((a,b))
            return movment_pos
        
        else:
            wind_val = self.enviorment.table[(position)]
            directions = [(-wind_val, 1), (-wind_val, -1)]
            for d in directions:
                (a, b) = (self.position[0] + d[0], self.position[1] + d[1])
                if a<=6 and a>=0 and b<=9 and b>=0:
                    movment_pos.append((a,b))
                elif b<=9 and b>=0 and a<0:
                    a = 0
                    movment_pos.append((a,b))
            return movment_pos


    def print_envr(self):
        envr = list(self.enviorment.__str__())
        if self.position != self.enviorment.start:
            envr[(self.position[0]*10+(self.position[1])+1)*2] = 'A'
        print(''.join(envr))






if __name__ == "__main__":
    agent = Agent()
    agent.print_envr()


