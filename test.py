import unittest
from operations import divide
class Testcases(unittest.TestCase):
    def testInteger(self):
        self.assertEqual(divide(15,3),5)
    def testNull(self):
        self.assertEqual(divide(0,0),0)

if __name__ == '__main__':
    unittest.main()