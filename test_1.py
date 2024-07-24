import unittest
from main1 import add, subtract, multiply, divide

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertNotEqual(add(10, -5), 4)
        self.assertEqual(add(-10, -5), -15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertNotEqual(subtract(10, -5), 13)
        self.assertEqual(subtract(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertNotEqual(multiply(10, -5), -52)
        self.assertEqual(multiply(-10, -5), 50)

    def test_divide_success(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertNotEqual(divide(10, -5), -3)
        self.assertEqual(divide(-10, -5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)  # правильная исключительная ситуация

        self.assertRaises(TypeError, divide, 10, 0)   #  неправильная исключительная ситуация

if __name__ == '__main1__':
    unittest.main()