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

    def test_name(self):
        """Selects and changes a player name and tests if the name was
        properly changed both times"""
        player1 = player.Player()
        name = player1.select_name()
        err = ""

        self.assertNotEqual(err, player1.name)
        self.assertEqual(player1.name, name)

        new_name = player1.change_name()
        self.assertNotEqual(name, new_name)
        self.assertEqual(player1.name, new_name)




if __name__ == '__main__':
    unittest.main()
