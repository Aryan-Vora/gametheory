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
        elif logs[-1][-1] == COOPERATE:
            return COOPERATE
        elif logs[-1][-1] == STEAL:
            return STEAL
    
class TitForTwoTats(Strategy):
    #cooperate on first move
    #if opponent cooperated on last move or second to last move, cooperate
    #else steal
    def make_move(self, logs):
        if not logs:
            return COOPERATE
        elif len(logs) == 1:
            return COOPERATE
        elif logs[-1][1] == COOPERATE or logs[-2][1] == COOPERATE:
            return COOPERATE
        return STEAL
    
class Grudger(Strategy):
    #store if opponent ever stole
    def __init__(self):
        self.stole = False

    #cooperate on first move
    #if opponent ever steals, steal for the rest of the game
    def make_move(self, logs):
        if not logs:
            return COOPERATE
        elif self.stole:
            return STEAL
        elif logs[-1][1] == STEAL:
            self.stole = True
            return STEAL
        return COOPERATE
    
class Random(Strategy):
    #randomly choose to cooperate or steal
    def make_move(self, logs):
        return random.choice([COOPERATE, STEAL])
    
class Pavlov(Strategy):
    def make_move(self, logs):
        if not logs or (logs[-1][0] == COOPERATE and logs[-1][1] == COOPERATE):
            return COOPERATE
        else:
            return not logs[-1][0]

class Adaptive(Strategy):
    def make_move(self, logs):
        cooperate_count = sum(1 for log in logs if log[1] == COOPERATE)
        steal_count = len(logs) - cooperate_count
        if cooperate_count >= steal_count:
            return COOPERATE
        else:
            return STEAL

class SuspiciousTitForTat(Strategy):
    def make_move(self, logs):
        if not logs:
            return STEAL
        else:
            return logs[-1][1]

class Forgiving(Strategy):
    def make_move(self, logs):
        if not logs:
            return COOPERATE
        if logs[-1][1] == STEAL:
            # 10% chance to forgive
            return random.choice([COOPERATE] * 1 + [STEAL] * 9)
        return COOPERATE
