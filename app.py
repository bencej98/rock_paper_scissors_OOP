import random

class Player():
    def __init__(self, name) -> None:
        self.choice = None
        self.score = 0
        self.name = name
        self.valid_choices = ["rock", "paper", "scissors"]

    def store_move(self) -> None:
        while True:
            self.choice = input(f"{self.name}, please choose your next move: ")
            if self.choice.lower() not in self.valid_choices:
                print("You can only choose from Rock, Paper or Scissors")
                continue
            else:
                print(self.choice)
                break
            
    def increase_score(self) -> None:
        self.score += 1

class Computer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name = "Computer"

    def store_move(self) -> None:
        self.choice = random.choice(self.valid_choices)
        




test = Player("Bence")
test.store_player_move()
