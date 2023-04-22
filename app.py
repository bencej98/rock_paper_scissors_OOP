class Player():
    def __init__(self, name) -> None:
        self.choice = None
        self.score = 0
        self.name = name

    def store_player_move(self):
        valid_choices = ["rock", "paper", "scissors"]
        while True:
            player_move = input(f"{self.name}, please choose your next move: ")
            if player_move.lower() not in valid_choices:
                print("You can only choose from Rock, Paper or Scissors")
                continue
            else:
                print(player_move)
                break


test = Player("Bence")
test.store_player_move()
