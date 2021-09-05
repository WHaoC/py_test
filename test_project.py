import unittest
import function_plus as fp

class TestPlusFunction(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(fp.func_plus(1,2), 3)
        self.assertEqual(fp.func_plus(3,99), 102)

    def test_negative(self):
        self.assertEqual(fp.func_plus(-1,-2), -3)
        self.assertEqual(fp.func_plus(-3,-99), -102)

    def test_zero(self):
        self.assertEqual(fp.func_plus(0,0), 0)
        self.assertEqual(fp.func_plus(3,0), 3)

if __name__ == "__main__":
    unittest.main()

