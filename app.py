import random

class Player():
    def __init__(self, name) -> None:
        self.choice = None
        self.score = 0
        self.name = name
        self.valid_choices = ["rock", "paper", "scissors"]

    def store_move(self) -> None:
        while True:
            self.choice = input(f"{self.name}, please choose your next choice: ")
            if self.choice.lower() not in self.valid_choices:
                print("You can only choose from Rock, Paper or Scissors")
                continue
            else:
                print(self.choice)
                break
            
    def increase_score(self) -> None:
        self.score += 1

class Computer(Player):
    def __init__(self) -> None:
        super().__init__("Computer")

    def store_move(self) -> None:
        self.choice = random.choice(self.valid_choices)
        print(self.choice)

class GameManager():
    def __init__(self, player, computer, ) -> None:
        self.player = player
        self.computer = computer
        self.is_game_over = False

    def decide_the_winner(self):
        if self.player.choice == self.computer.choice:
            print("It's a tie")
        elif (self.player.choice == "rock" and self.computer_player.choice == "scissors") or \
             (self.player.choice == "paper" and self.computer_player.choice == "rock") or \
             (self.player.choice == "scissors" and self.computer_player.choice == "paper"):
            self.player.increase_score()
            print(f"{self.player.name} won the round!")
        else:
            self.computer.increase_score()
            print(f"{self.computer.name} won the round!")

    

    
player_name = input("Choose your name: ")
test = Player(player_name)
test.store_move()
computer = Computer()
computer.store_move()
