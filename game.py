COOPERATE = True
STEAL = False
class Game:
    def simulate(self, strategy1, strategy2, rounds=100, file=None):
        logs = []
        score1, score2 = 0, 0
        name1 = type(strategy1).__name__
        name2 = type(strategy2).__name__
        for _ in range(rounds):
            move1 = strategy1.make_move(logs)
            move2 = strategy2.make_move(logs)

            if move1 and move2:
                score1 += 3
                score2 += 3
                logs.append(([name1, COOPERATE], [name2, COOPERATE]))
            elif not move1 and not move2:
                score1 += 1
                score2 += 1
                logs.append(([name1, STEAL], [name2, STEAL]))
            elif move1 and not move2:
                score2 += 5
                logs.append(([name1, COOPERATE], [name2, STEAL]))
            else:
                score1 += 5
                logs.append(([name1, STEAL], [name2, COOPERATE]))
        if file:
            with open(file, "w") as f:
                f.write(f"{type(strategy1).__name__}: {score1}\n")
                f.write(f"{type(strategy2).__name__}: {score2}\n")
                for result in logs:
                    f.write(f'{name1} {"cooperates" if result[0][1] else "steals"} and {name2} {"cooperates" if result[1][1] else "steals"}\n')
        return logs, score1, score2, [name1, score1, name2, score2]
