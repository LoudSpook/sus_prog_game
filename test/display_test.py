

import unittest
from game import display

class TestDisplay(unittest.TestCase):
 
    def test_init_default_object(self):
        displayer = display.Display()
        self.assertIsInstance(displayer, display.Display)
        
        res = display.display_rules
        exp = ['1. Do not cheat', '2. Do not swear', '3. Do not fight', '4. Have fun']
        self.assertListEqual(res,exp)
        
if __name__ == '__main__':
    unittest.main()