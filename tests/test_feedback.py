import sys
import unittest

sys.path.append("../")
from feedback import Feedback


class TestFeedback(unittest.TestCase):
    def setUp(self):
        self.feedback_1: Feedback = Feedback([1, 2, 3], [1, 2, 3])
        self.feedback_2: Feedback = Feedback([1, 2, 3], [1, 0, 0])
        self.feedback_3: Feedback = Feedback([1, 2, 3], [3, 1, 2])
        self.feedback_4: Feedback = Feedback([1, 3, 3], [0, 3, 3])
        self.feedback_5: Feedback = Feedback([1, 2, 3], [4, 4, 4])

    def test_generate_feedback(self):
        self.assertEqual(
            self.feedback_1.generate_feedback(),
            "3 correct number(s) and 3 correct location(s)",
        )
        self.assertEqual(
            self.feedback_2.generate_feedback(),
            "1 correct number(s) and 1 correct location(s)",
        )
        self.assertEqual(
            self.feedback_3.generate_feedback(),
            "3 correct number(s) and 0 correct location(s)",
        )
        self.assertEqual(
            self.feedback_4.generate_feedback(),
            "2 correct number(s) and 2 correct location(s)",
        )
        self.assertEqual(self.feedback_5.generate_feedback(), "All incorrect!")

    def test_correct_numbers_count(self):
        self.assertEqual(self.feedback_1.correct_numbers_count(), 3)
        self.assertEqual(self.feedback_2.correct_numbers_count(), 1)
        self.assertEqual(self.feedback_3.correct_numbers_count(), 3)
        self.assertEqual(self.feedback_4.correct_numbers_count(), 2)
        self.assertEqual(self.feedback_5.correct_numbers_count(), 0)

    def test_correct_location_count(self):
        self.assertEqual(self.feedback_1.correct_location_count(), 3)
        self.assertEqual(self.feedback_2.correct_location_count(), 1)
        self.assertEqual(self.feedback_3.correct_location_count(), 0)
        self.assertEqual(self.feedback_4.correct_location_count(), 2)
        self.assertEqual(self.feedback_5.correct_location_count(), 0)


if __name__ == "__main__":
    unittest.main()
