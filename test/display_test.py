
import unittest
from game import display

class TestDisplay(unittest.TestCase):
 
    def test_display_rules(self):
        """Testing if rules are displayed"""
        displayer = display.Display()
        rules = displayer.display_rules()
        
        expected = ['1. Do not cheat', '2. Do not swear', '3. Do not fight', '4. Have fun']
        self.assertListEqual(rules,expected)
    
    def test_display_graphics(self):
        """Testing if graphics are displayed"""
        displayer = display.Display()
        testsentence = ""
        
        res = displayer.display_graphics(testsentence)
        exp = displayer.display_graphics()
        self.assertEqual(res,exp)
        
    
    def test_display_highscore(self):
        """Tests if it actually displays anything"""
        displayer = display.Display()
        exp = displayer.display_highscore()
        err = ''
        self.assertNotEqual(exp, err)

        
        
if __name__ == '__main__':
    unittest.main()