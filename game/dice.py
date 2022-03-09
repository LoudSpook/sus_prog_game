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
        """Roll a dice."""
        roll = random.randint(1, self.faces)
        self.rolls_made += 1

        return roll

    def get_rolls_made(self):
        """Return rolls_made."""
        return self.rolls_made

    def clean_rolls_made(self):
        """Reset rolls_made back to 0."""
        self.rolls_made = 0
        return self.rolls_made


if __name__ == '__main__':
    die = Dice()
