from player import Player
from utils.validate_input import is_valid_1or2, is_valid_code


class CLI:
    def display_border(self) -> None:
        print("=" * 30)

    def display_code_cover(self) -> None:
        line: str = "=" * 30
        for _ in range(100):
            print(line)

    def display_code_created(self) -> None:
        print("The CODEMAKER has created the code!")

    def display_feedback(self, feedback):
        print(feedback)

    def display_game_intro(self) -> None:
        print("Welcome to Mastermind!")

    def display_game_over(self) -> None:
        print("Game Over! Thank you for playing.")

    def display_game_start(self) -> None:
        print("Game Start!")

    def display_guess(self, guess) -> None:
        print(f"Your guess is: {guess}")

    def display_guesses_left(self, guesses_left):
        print(f"You have {guesses_left} guess(es) left!")

    def display_right_guess(self) -> None:
        print("The CODEBREAKER guessed correctly!")

    def display_winner(self, winner: Player) -> None:
        print(f"{winner.name} the {winner.role} has won!")

    def display_wrong_guess(self) -> None:
        print("Incorrect guess!")

    def get_choice(self, choice_map: dict[str, str]) -> str:
        while True:
            try:
                choice: str = input().strip()
                if is_valid_1or2(choice):
                    return choice_map[choice]

            except ValueError as ve:
                print(f"{ve} Please try again.")

    def get_code(self, player_name, count, min_val, max_val) -> list[int]:
        print(
            f"{player_name}, you are the CODEMAKER. Please enter {count} number(s), each number between {min_val} and {max_val} and separated by a single space. Duplicate numbers are allowed."
        )
        while True:
            try:
                raw_input: str = input().strip()

                if is_valid_code(raw_input, count, min_val, max_val):
                    return [int(num_str) for num_str in raw_input.split(" ")]

            except ValueError as ve:
                print(f"{ve} Please try again.")

    def get_difficulty(self) -> int:
        while True:
            try:
                print("Select a difficulty level. Enter a number between 1 and 10: ")
                difficulty = input().strip()
                if not difficulty.isdigit():
                    raise ValueError("Value must be an integer.")
                elif int(difficulty) < 1 or int(difficulty) > 10:
                    raise ValueError("Value must be between 1 and 10.")
                return int(difficulty)
            except ValueError as ve:
                print(f"{ve} Please try again.")

    def get_guess(self, player_name, count, min_val, max_val):
        print(
            f"{player_name}, you are the CODEBREAKER. Please enter {count} number(s), each number between {min_val} and {max_val} and separated by a single space."
        )
        while True:
            try:
                raw_input: str = input().strip()

                if is_valid_code(raw_input, count, min_val, max_val):
                    return [int(num_str) for num_str in raw_input.split(" ")]

            except ValueError as ve:
                print(f"{ve} Please try again.")

    def get_opponent_type(self, player1_name: str) -> str:
        print(
            f"{player1_name}, do you want your opponent to be a computer or another human player?\nEnter 1 for a COMPUTER opponent\nEnter 2 for a HUMAN opponent"
        )
        opponent_type_map: dict[str, str] = {"1": "COMPUTER", "2": "HUMAN"}
        opponent_type: str = self.get_choice(opponent_type_map)
        return opponent_type

    def get_player_name(self, player_num) -> str:
        print(f"Player{player_num}, please enter your name: ")
        return input().strip()

    def get_player1_role(self, player1_name: str) -> str:
        print(
            f"{player1_name}, do you want to be the CODEBREAKER or the CODEMAKER?\nEnter 1 for CODEBREAKER\nEnter 2 for CODEMAKER"
        )
        role_map: dict[str, str] = {"1": "CODEBREAKER", "2": "CODEMAKER"}
        role: str = self.get_choice(role_map)
        return role

    def game_setup_prompts(self) -> dict[str, int | dict]:
        difficulty: int = self.get_difficulty()

        player1_name: str = self.get_player_name(1)
        player1_role: str = self.get_player1_role(player1_name)
        player1_type: str = "HUMAN"

        player2_type: str = self.get_opponent_type(player1_name)
        player2_name: str = (
            self.get_player_name(2) if player2_type == "HUMAN" else "TARS Computer"
        )
        player2_role: str = (
            "CODEMAKER" if player1_role == "CODEBREAKER" else "CODEBREAKER"
        )

        return {
            "difficulty": difficulty,
            player1_role: {
                "name": player1_name,
                "role": player1_role,
                "kind": player1_type,
            },
            player2_role: {
                "name": player2_name,
                "role": player2_role,
                "kind": player2_type,
            },
        }
