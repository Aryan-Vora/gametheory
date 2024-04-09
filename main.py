from strategies import *
from game import Game
def match(strategy1, strategy2, rounds=100, file=None):
    game = Game()
    return game.simulate(strategy1, strategy2, rounds, file)
def tournament(strategies):
    scores = {}
    log = []
    for i in range(len(strategies)):
        for j in range(len(strategies)):

            strategy1 = strategies[i]
            strategy2 = strategies[j]
            game = Game()
            _, score1, score2, _ = game.simulate(strategy1(), strategy2())
            name1 = type(strategy1()).__name__
            name2 = type(strategy2()).__name__
            log.append((name1, name2, score1, score2))
            if name1 not in scores:
                scores[name1] = score1
            else:
                scores[name1] += score1
    scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    return scores, log

    

def main():
    pass

if __name__ == "__main__":
    main()
