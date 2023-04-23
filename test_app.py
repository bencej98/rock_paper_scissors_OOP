import unittest
import sys
sys.path.append("C:\home\bencejenei\rock_paper_scissors_OOP")
from app import Player, Computer, GameManager


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self) -> None: 
        self.player = Player("player")
        self.computer_player = Computer()
        self.current_game = GameManager(self.player, self.computer_player)

    def test_if_computer_choice_is_valid(self):
        self.current_game.computer.get_move()
        self.assertIn(self.current_game.computer.choice, self.current_game.computer.valid_choices)
