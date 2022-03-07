"""Unittesting"""

import unittest
from game import player

class TestPlayerClass(unittest.TestCase):
    """Testing the class."""

    def test_init_player_object(self):
        """Instantiate a player object and test its base values."""
        player1 = player.Player()
        self.assertIsInstance(player1, player.Player)

        res1 = player1.name
        exp1 = ""
        self.assertEqual(res1, exp1)

        res2 = player1.score
        exp2 = 0
        self.assertEqual(res2, exp2)

    def test_select_name(self): #MÖJLIGTVIS GÖR SÅ DEN KOLLAR OM NAMNET FAKTISKT ÄNDRAS MED
        """Select a player name and tests if the name is empty
        (empty is not allowed)."""
        player1 = player.Player()
        name = player1.select_name()
        err = ""

        self.assertNotEqual(err, name)

    #def test_change_name(self):
        #"""Tries changing the player name and checks if it actually changes."""
        #player1 = player.Player()
        #name1 = player1.select_name()
        #name2




if __name__ == '__main__':
    unittest.main()
