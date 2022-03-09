

import unittest
from game import display

class TestDisplay(unittest.TestCase):
 
    def test_display_rules(self):
        displayer = display.Display()
        rules = displayer.display_rules()
        
        exp = ['1. Do not cheat', '2. Do not swear', '3. Do not fight', '4. Have fun']
        self.assertListEqual(rules,exp)
    
    def test_display_graphics(self):
        displayer = display.Display()
        blank = ''
        self.assertNotEqual(blank,displayer.display_graphics)
        
        
if __name__ == '__main__':
    unittest.main()