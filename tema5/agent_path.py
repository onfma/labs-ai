import copy
import numpy as np

class Q_table:
    def __init__(self) -> None:
        self.table = np.zeros((7, 10), dtype=int)
        self.start = (3,0)
        self.destination = (3,7)
        self.agent = self.start
        self.wind = [0,0,0,0,0,0,0,0,0,0] 

    def set_wind(self, array):  #set wind on board
        self.wind = array
        for j in range(10):
            if array[j] != 0:
                for i in range(7):
                    self.table[i, j] = array[j]

    def set_start(self, tuple):     #redefine start
        self.start = tuple

    def set_destination(self, tuple):   #redefine end
        self.destination = tuple

    def __str__(self) -> str:   #print board status
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
        self.environment = Q_table()
        self.environment.set_wind([0,0,0,1,1,1,2,2,1,0])
        self.position = self.environment.start       #define environment
        self.learning_rate = 0.01
        self.path = []
        self.Q_val = np.zeros((7,10,4))

    def next_state(self, curent_pos, action):   #action: 0 = N, 1 = E, 2 = S, 3 = W
        if self.environment.table[(curent_pos)] == 0:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            d = directions[action]
            a, b = curent_pos[0] + d[0], curent_pos[1] + d[1]
            a = max(0, min(a, 6))
            b = max(0, min(b, 9)) 
            return a, b
        else:
            wind_val = self.environment.table[(curent_pos)]
            directions = [(-(wind_val + 1), 0), (-wind_val, 1), (-(wind_val-1), 0), (-wind_val, -1)]
            d = directions[action]
            a, b = curent_pos[0] + d[0], curent_pos[1] + d[1]
            a = max(0, min(a, 6))
            b = max(0, min(b, 9)) 
            return a, b
        

    def Q_learning_algo(self):
         for _ in range(200):
            self.environment.agent = self.environment.start
            state = self.environment.agent

            while state != self.environment.destination:
                #select action with the biggest Q val with prob = learning rate
                rand = np.random.rand()
                if rand < self.learning_rate:
                    action = np.random.randint(4)
                else:
                    action = np.argmax(self.Q_val[state[0], state[1]])

                next_state = self.next_state(state, action)

                self.calc_q_val(state, action, next_state)

                state = next_state

    def calc_q_val(self, state, action, next_state):
        alpha = 0.9
        gamma = 0.9
        reward = -1
        if state == self.environment.destination:
            reward = 1000
        max_next_q = np.max(self.Q_val[next_state[0], next_state[1]])
        current_q = self.Q_val[state[0], state[1], action]
        q = current_q + alpha * (reward + gamma * max_next_q - current_q)
        self.Q_val[state[0], state[1], action] = q

    def print_polic(self):
        directions = ['N','E','S','W']
        for i in range(7):
            for j in range(10):
                indx = np.argmax(self.Q_val[i][j])
                print(f"{directions[indx]} ", end = "")
            print()


if __name__ == "__main__":
    agent = Agent()
    agent.Q_learning_algo()
    print(agent.environment)
    agent.print_polic()


