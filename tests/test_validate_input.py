import sys
import unittest

sys.path.append("../")
from utils.validate_input import is_valid_1or2, is_valid_code


class TestValidateInput(unittest.TestCase):
    def test_is_valid1or2(self):
        self.assertTrue(is_valid_1or2("1"))
        self.assertTrue(is_valid_1or2("2"))

    def test_is_valid1or2_exception(self):
        self.assertRaises(ValueError, is_valid_1or2, "adsfasdf")
        self.assertRaises(ValueError, is_valid_1or2, "23")
        self.assertRaises(ValueError, is_valid_1or2, "0")
        self.assertRaises(ValueError, is_valid_1or2, "0sdf")

    def test_is_valid_code(self):
        self.assertTrue(is_valid_code("1 2 3", 3, 0, 7))
        self.assertTrue(is_valid_code("1 2 3 4", 4, 0, 7))

    def test_is_valid_code_exception(self):
        self.assertRaises(ValueError, is_valid_code, "9", 3, 0, 7)
        self.assertRaises(ValueError, is_valid_code, "1 2", 1, 0, 7)
        self.assertRaises(ValueError, is_valid_code, "1  2  3", 3, 0, 7)
        self.assertRaises(ValueError, is_valid_code, "asdas  2  3", 3, 0, 7)


if __name__ == "__main__":
    unittest.main()
