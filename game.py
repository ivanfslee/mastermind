from cli import CLI
from feedback import Feedback
from player import Player


class Game:
    def __init__(self, cli: CLI, game_setup: dict[str, int | dict]) -> None:
        self.cli: CLI = cli
        self.codebreaker: Player = Player(
            game_setup["CODEBREAKER"]["name"],
            game_setup["CODEBREAKER"]["role"],
            game_setup["CODEBREAKER"]["kind"],
        )
        self.codemaker: Player = Player(
            game_setup["CODEMAKER"]["name"],
            game_setup["CODEMAKER"]["role"],
            game_setup["CODEMAKER"]["kind"],
        )
        self.guesses_left: int = 10
        self.code_length: int = game_setup["difficulty"]
        self.code_min_val: int = 0
        self.code_max_val: int = 7

    def play(self) -> None:
        self.cli.display_game_start()

        code: list[int] = self.codemaker.generate_code(
            self.cli, self.code_length, self.code_min_val, self.code_max_val
        )

        # We are printing the code here for debugging purposes.
        print("code generated! code is: ", code)

        if self.codebreaker.kind == "HUMAN":
            self.cli.display_code_cover()

        self.cli.display_code_created()

        winner: Player = self.codemaker

        while self.guesses_left > 0:
            self.cli.display_border()
            self.cli.display_guesses_left(self.guesses_left)

            guess: list[int] = self.codebreaker.generate_guess(
                self.cli, self.code_length, self.code_min_val, self.code_max_val
            )

            self.cli.display_guess(guess)
            feedback: str = Feedback(guess, code).generate_feedback()
            self.cli.display_feedback(feedback)

            if guess == code:
                self.cli.display_right_guess()
                winner = self.codebreaker
                break
            else:
                self.cli.display_wrong_guess()
                self.guesses_left -= 1

        self.cli.display_winner(winner)
        self.cli.display_game_over()
