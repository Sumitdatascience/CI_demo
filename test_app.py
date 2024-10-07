import unittest
from app import add, sub, mul

class TestMatchFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,5),10)
        self.assertEqual(add(6,5),11)

    def test_sub(self):
        self.assertEqual(sub(5,5),0)
        self.assertEqual(sub(6,5),1)   

    def test_mul(self):
        self.assertEqual(mul(5,5),25)
        self.assertEqual(mul(6,5),30)    


if __name__ == '__main__':
    unittest.main()         