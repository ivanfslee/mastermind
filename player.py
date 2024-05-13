import random

from utils.get_random_numbers import generate_random_numbers


class Player:
    def __init__(self, name, role, kind):
        self.name = name
        self.role = role
        self.kind = kind

    def generate_code(self, cli, count, min_val, max_val) -> list[int]:
        code: list[int] = []
        if self.kind == "HUMAN":
            code = cli.get_code(self.name, count, min_val, max_val)
        else:
            code = generate_random_numbers(count, min_val, max_val)
        return code

    def generate_guess(self, cli, count, min_val, max_val) -> list[int]:
        guess: list[int] = []
        if self.kind == "HUMAN":
            guess = cli.get_guess(self.name, count, min_val, max_val)
        else:
            guess = [random.randint(min_val, max_val) for _ in range(count)]
        return guess

    def __repr__(self) -> str:
        return str(self.__dict__)
