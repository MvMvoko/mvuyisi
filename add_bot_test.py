import unittest
from add_bot import AddBot

class AddBotTest(unittest.TestCase):
    
    def testAdd1(self):
        adder = AddBot()
        self.assertEqual(adder.Add(3, 3), 6)

if __name__ == "__main__":
    unittest.main()
