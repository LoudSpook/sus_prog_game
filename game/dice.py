"""Handle things related to the dice."""

import random

class Dice():
    """Handle the dice object."""

    faces = 6

    def __init__(self):
        """Set default values to the object."""
        self.rolls_made = 0
        random.seed()

    def roll_dice(self):
        """Rolls a dice."""
        roll = random.randint(1, self.faces)
        self.rolls_made += 1

        return roll

    def get_rolls_made(self):
        return self.rolls_made



if __name__ == '__main__':
    die = Dice()
    roll = die.roll_dice()
    print(roll)
