
import io
from itertools import count
import unittest
import sys
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
        testsentence = 'Testing'
        displayer = display.Display()
        res = displayer.display_graphics(testsentence)
        
        """Prepare to capture the output"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        
        """Call the method """
        displayer.display_graphics(testsentence)
        
        """Reset the capture"""
        sys.stdout = sys.__stdout__
        
        """Get the catured output"""
        output = capturedOutput.getvalue()
        
        """See if the graphic is printed"""
        self.assertTrue(str(res) in output)
    
    def test_display_highscore(self):
        """Uses a test list to test display_highscore"""
        displayer = display.Display()
        test_list = [('Pelle', 50),('Anders', 20),('Bengt', 30)]
        exp = displayer.display_highscore(test_list)
        err = ''
        self.assertNotEqual(exp, err)

        
        
if __name__ == '__main__':
    unittest.main()