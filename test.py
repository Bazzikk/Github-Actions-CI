import unittest
import example


class TestCase(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(example.addition(1, 2), 3)

    def test_sub_1(self):
        self.assertEqual(example.subtraction(2, 1), 1)

    def test_mul_1(self):
        self.assertEqual(example.multiplication(2, 1), 2)

    def test_div_1(self):
        self.assertEqual(example.division(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
