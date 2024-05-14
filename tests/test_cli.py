import io
import sys
import unittest
from unittest.mock import patch

sys.path.append("../")
from cli import CLI
from player import Player


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli_1: CLI = CLI()

    def assert_stdout(self, expected_output, test_method, *args):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        test_method(*args)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_border(self):
        self.assert_stdout("=" * 30 + "\n", self.cli_1.display_border)

    def test_display_code_cover(self):
        print_out = ("=" * 30 + "\n") * 100
        self.assert_stdout(print_out, self.cli_1.display_code_cover)

    def test_display_code_created(self):
        self.assert_stdout(
            "The CODEMAKER has created the code!\n", self.cli_1.display_code_created
        )

    def test_display_feedback(self):
        self.assert_stdout(
            "3 correct number(s) and 3 correct location(s)\n",
            self.cli_1.display_feedback,
            "3 correct number(s) and 3 correct location(s)",
        )

    def test_display_game_intro(self):
        self.assert_stdout("Welcome to Mastermind!\n", self.cli_1.display_game_intro)

    def test_display_game_over(self):
        self.assert_stdout(
            "Game Over! Thank you for playing.\n", self.cli_1.display_game_over
        )

    def test_display_game_start(self):
        self.assert_stdout("Game Start!\n", self.cli_1.display_game_start)

    def test_display_guess(self):
        self.assert_stdout(
            "Your guess is: [1, 2, 3]\n", self.cli_1.display_guess, "[1, 2, 3]"
        )

    def test_display_guesses_left(self):
        self.assert_stdout(
            "You have 5 guess(es) left!\n", self.cli_1.display_guesses_left, "5"
        )

    def test_display_right_guess(self):
        self.assert_stdout(
            "The CODEBREAKER guessed correctly!\n", self.cli_1.display_right_guess
        )

    def test_display_winner(self):
        self.assert_stdout(
            "Ivan the CODEBREAKER has won!\n",
            self.cli_1.display_winner,
            Player("Ivan", "CODEBREAKER", "HUMAN"),
        )

    def test_display_wrong_guess(self):
        self.assert_stdout("Incorrect guess!\n", self.cli_1.display_wrong_guess)


if __name__ == "__main__":
    unittest.main()
