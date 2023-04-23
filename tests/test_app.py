import unittest
from app import Player, Computer, GameManager


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player("Player")
        self.computer_player = Computer()
        self.current_game = GameManager(self.player, self.computer_player)
