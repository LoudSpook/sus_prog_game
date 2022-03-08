"""Unittesting"""

import unittest
from game import dice

class TestDiceClass(unittest.TestCase):
    """Testing the calss."""

    def test_init_dice_object(self):
        """Instantiate a dice object and test its values"""
        die = dice.Dice()
        self.assertIsInstance(die, dice.Dice())

        res = die.faces
        exp = 6
        self.assertEqual(res, exp)
