"""Handles most things related to the player(s)."""


class Player():
    """Handles the player object."""

    def __init__(self):
        self.name = ""
        self.score = 0

    def select_name(self):
        """Lets players select their name."""
        keep_going = True
        forbidden_word = "BOT"

        while keep_going:
            self.name = input("Select your name: ")

            if self.name:
                if forbidden_word not in self.name:
                    keep_going = False
                else:
                    print('Name can not contain "BOT"!')
            else:
                print("Name can not be empty!")

        print("Name set!")
        return self.name

    def change_name(self):
        """Lets players change their names"""
        current_name = self.name
        new_name = self.select_name()

        if current_name == new_name:
            print("You already have this name!")
            self.name = current_name
        else:
            print("Name changed!")

        return self.name

    def add_score(self, rolls):
        """Adds a players score from that round to their total"""
        self.score += rolls

        return self.score




if __name__ == '__main__':
    #Used for testing purposes
    player = Player()
    name = player.select_name()
    print(name)

    name = player.change_name()
    print(name)

    print("Your score is:", player.score)
    score = player.add_score(3)
    print("Your score is now:", score)
