import unittest
from main import check

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

if __name__ == '__main__':
    unittest.main()
