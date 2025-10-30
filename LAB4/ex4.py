import random

class DiceGame:
    def __init__(self, players, rounds):
        self.players = players
        self.rounds = rounds
        self.scores = {player: 0 for player in players}

    def play_round(self):
        print("\n--- New Round ---")
        for player in self.players:
            roll = random.randint(1, 6)
            self.scores[player] += roll
            print(f"{player} rolled a {roll}")

    def display_scores(self):
        print("\nCurrent Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

    def winner(self):
        max_score = max(self.scores.values())
        top_players = []
        for player, score in self.scores.items():
            if score == max_score:
                top_players.append(player)

        # handler pt remiza
        while len(top_players) > 1:
            print("\nTie between:", ", ".join(top_players))
            print("Rolling again to decide the winner...")
            rolls = {p: random.randint(1, 6) for p in top_players}
            for p, r in rolls.items():
                print(f"{p} rolled {r}")
            winner = max(rolls, key=rolls.get)
            print(f"\nWinner after tie-break: {winner}")
            return winner
        else:
            winner = top_players[0]
            print(f"\nWinner: {winner}")
            return winner


# Example usage:
players = ["Nicusor", "Ilie", "Marcel"]
rounds = int(input("Enter number of rounds: "))

game = DiceGame(players, rounds)

for _ in range(rounds):
    game.play_round()
    game.display_scores()

game.winner()
