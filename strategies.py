from abc import ABC, abstractmethod
import random
COOPERATE = True
STEAL = False

class Strategy(ABC):
    @abstractmethod
    def make_move(self):
        pass

class AlwaysCooperate(Strategy):
    def make_move(self, logs):
        return COOPERATE

class AlwaysSteal(Strategy):
    def make_move(self, logs):
        return STEAL 
    
class TitForTat(Strategy):
    def make_move(self, logs):
        #cooperate on first move
        #if opponent cooperated on last move, cooperate
        #if opponent stole on last move, steal
        if not logs:
            return COOPERATE 
        turn = 0 if logs[0][0][0] == type(self).__name__ else 1
        if logs[-1][turn][1] == COOPERATE:
            return COOPERATE
        if logs[-1][turn][1] == STEAL:
            return STEAL

class Random(Strategy):
    def make_move(self, logs):
        return random.choice([COOPERATE, STEAL])
    
class TitForTwoTats(Strategy):
    def make_move(self, logs):
        #cooperate on first move
        #if opponent cooperated on last two moves, cooperate
        #if opponent stole on last two moves, steal
        if not logs:
            return COOPERATE
        turn = 0 if logs[0][0][0] == type(self).__name__ else 1
        if len(logs) < 2:
            if logs[-1][turn][1] == COOPERATE:
                return COOPERATE
            if logs[-1][turn][1] == STEAL:
                return STEAL
        if logs[-1][turn][1] == COOPERATE and logs[-2][turn][1] == COOPERATE:
            return COOPERATE
        if logs[-1][turn][1] == STEAL and logs[-2][turn][1] == STEAL:
            return STEAL
        
           


#[([name1, move1], [name2, move2])]