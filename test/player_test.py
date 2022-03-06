"""Unittesting"""

import unittest
from game import player

class TestPlayerClass(unittest.TestCase):
    """Testing the class"""

    def test_init_player_object(self):
        """Instantiate a player object"""
        player1 = player.Player()
        self.assertIsInstance(player, player.Player)


if __name__ == '__main__':
    unittest.main()
