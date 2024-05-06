import unittest
from unittest.mock import patch, Mock
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import game

class TestGame(unittest.TestCase):


    @patch('builtins.input', side_effect=["1", "mocked_word_to_guess"])
    @patch('game.HangmanTemplates.getAnimalWords', return_value="mocked_word_to_guess")
    @patch('game.HangmanTemplates.get_guesses', return_value="mocked_hangman_visual")
    def test_game_one_player(self, mock_getAnimalWords, mock_get_guesses, mock_input):
        Players1_game = game()
        Players1_game.game()

        self.assertTrue(mock_getAnimalWords.called)
        self.assertTrue(mock_get_guesses.called)
        self.assertTrue(mock_input.called)



    @patch('builtins.input', side_effect=["2", "test", "t", "e", "s", "t"])
    @patch('game.HangmanTemplates.get_guesses', return_value="mocked_hangman_visual")
    @patch('game.HangmanTemplates.getAnimalWords', return_value="mocked_word_to_guess")
    def test_game_two_players(self, mock_getAnimalWords, mock_get_guesses, mock_input):

        Players2_game = game()
        Players2_game.game()

        self.assertFalse(mock_getAnimalWords.called)
        self.assertTrue(mock_get_guesses.called)
        self.assertTrue(mock_input.called)

    def test_game_quit(self):
        test_game = game()
        game_over = test_game.game_quit()
        self.assertTrue(game_over)

    def test_game_won(self):
        test_game = game()
        game_over = test_game.game_won()
        self.assertTrue(game_over)


if __name__ == '__main__':
    unittest.main()