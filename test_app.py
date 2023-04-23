import unittest
import sys
sys.path.append("C:\home\bencejenei\rock_paper_scissors_OOP")
from app import Player, Computer, GameManager
from unittest.mock import patch
from io import StringIO


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self) -> None: 
        self.player = Player("player")
        self.computer = Computer()
        self.current_game = GameManager(self.player, self.computer)

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
        self.computer.choice = 'scissors'
        self.current_game.decide_the_winner()
        self.assertEqual(mock_stdout.getvalue(), f'{self.player.name} won the round!\n')

    def test_check_game_over_if_player_has_3_points(self):
        self.player.score = 3
        self.current_game.check_the_score()
        self.assertTrue(self.current_game.is_game_over)

    
    def test_check_game_over_if_computer_has_3_points(self):
        self.computer.score = 3
        self.current_game.check_the_score()
        self.assertTrue(self.current_game.is_game_over)