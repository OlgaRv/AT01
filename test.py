
import unittest
from main import check, add, subtract, multiply, divide, remainder

class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertTrue(not check(3))
        self.assertTrue(not check(7))
        self.assertTrue(not check(115))


        self.assertFalse(check(1))
        self.assertFalse(check(5))
        self.assertFalse(check(9))

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

    def test_remainder(self):
        self.assertEqual(remainder(10, 5), 0)
        self.assertEqual(remainder(10, -5), 0)
        self.assertEqual(remainder(10, 1), 0)

    def test_remainder_by_zero(self):
        self.assertRaises(ValueError, remainder, 10, 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)  # правильная исключительная ситуация


if __name__ == '__main__':
    unittest.main()
