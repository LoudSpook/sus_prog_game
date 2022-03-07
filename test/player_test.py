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

    def test_select_name(self):
        """Select a player name and check if variable name changed correctly"""
        player1 = player.Player()

        player1.name = player1.select_name()
        err = ""

        self.assertNotEqual(err, player1.name)
        self.assertEqual(player1.name, player1.select_name)




if __name__ == '__main__':
    unittest.main()
