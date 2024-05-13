class Feedback:
    def __init__(self, code: list[int], guess: list[int]):
        self.code: list[int] = code
        self.guess: list[int] = guess

    def generate_feedback(self) -> str:
        numbers_count: int = self.correct_numbers_count()
        location_count: int = self.correct_location_count()

        if numbers_count == 0:
            return "All incorrect!"
        else:
            return f"{numbers_count} correct number(s) and {location_count} correct location(s)"

    def correct_numbers_count(self) -> int:
        """Gets the count of correct numbers in the codebreaker's guess"""
        numbers_count: int = 0
        correct_numbers: list[int] = self.code.copy()
        for number in self.guess:
            if number in correct_numbers:
                numbers_count += 1
                number_idx: int = correct_numbers.index(number)
                correct_numbers.pop(number_idx)
        return numbers_count

    def correct_location_count(self) -> int:
        """Gets the count of the correct numbers in the correct location in the codebreaker's guess"""
        location_count: int = 0
        for idx in range(len(self.guess)):
            guess_num: int = self.guess[idx]
            code_num: int = self.code[idx]
            if guess_num == code_num:
                location_count += 1
        return location_count
