import unittest
import sys
sys.path.append("C:\home\bencejenei\rock_paper_scissors_OOP")
from app import Player, Computer, GameManager
from unittest.mock import patch
from io import StringIO


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self) -> None: 
        self.player = Player("player")
        self.computer_player = Computer()
        self.current_game = GameManager(self.player, self.computer_player)

    def test_if_computer_choice_is_valid(self):
        self.current_game.computer.get_move()
        self.assertIn(self.current_game.computer.choice, self.current_game.computer.valid_choices)

    def test_get_move_of_the_player(self):
        with patch('builtins.input', side_effect=['rock']):
            self.player.get_move()
            self.assertEqual(self.player.choice, 'rock')
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_decide_the_winner(self, mock_stdout):
        self.player.choice = 'rock'
        self.computer_player.choice = 'scissors'
        self.current_game.decide_the_winner()
        self.assertEqual(mock_stdout.getvalue(), f'{self.player.name} won the round!\n')