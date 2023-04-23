import random

class Player():
    def __init__(self, name) -> None:
        self.choice = None
        self.score = 0
        self.name = name
        self.valid_choices = ["rock", "paper", "scissors"]

    def get_move(self) -> None:
        """Gets the current move of the player"""
        while True:
            self.choice = input(f"{self.name}, please choose your next choice: ").lower()
            if self.choice not in self.valid_choices:
                print("You can only choose from Rock, Paper or Scissors")
                continue
            else:
                break
            
    def increase_score(self) -> None:
        self.score += 1

class Computer(Player):
    def __init__(self) -> None:
        super().__init__("Computer")

    def get_move(self) -> None:
        self.choice = random.choice(self.valid_choices)
        
class GameManager():
    def __init__(self, player, computer, ) -> None:
        self.player = player
        self.computer = computer
        self.is_game_over = False

    def decide_the_winner(self) -> None:
        """Based on the player's and computer's choice decides the winner of the current round"""
        if self.player.choice == self.computer.choice:
            print("It's a tie")
        elif (self.player.choice == "rock" and self.computer.choice == "scissors") or \
             (self.player.choice == "paper" and self.computer.choice == "rock") or \
             (self.player.choice == "scissors" and self.computer.choice == "paper"):
            self.player.increase_score()
            print(f"{self.player.name} won the round!")
        else:
            self.computer.increase_score()
            print(f"{self.computer.name} won the round!")

    def check_the_score(self) -> None:
        """After every round checks the current score of each player"""
        if self.player.score == 3:
            print(f"{self.player.name} wins the game! Congrats!")
            self.is_game_over = True
        elif self.computer.score == 3:
            print(f"{self.computer.name} wins the game!")
            self.is_game_over = True

    def start_game(self) -> None:
        """Manages the game with all the related functions"""
        print("Prepare yourself! The game against the computer has started!")
        while self.is_game_over is False:
            self.player.get_move()
            self.computer.get_move()
            self.decide_the_winner()
            print(f" Your score:{self.player.score} ||| Computer's score:{self.computer.score}")
            self.check_the_score()

player_name = input("Type your name here: ")
player = Player(player_name)
computer = Computer()
current_game = GameManager(player, computer)

if __name__ == "__main__":
    current_game.start_game()

