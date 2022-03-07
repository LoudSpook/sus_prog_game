"""Handles most things related to the player(s)."""


class Player():
    """Handles the player object."""

    name = ""
    score = 0

    def select_name(self):
        """Lets players select their name."""
        keep_going = True
        forbidden_word = "BOT"

        while keep_going:
            name = input("Select your name: ")

            if forbidden_word not in name:
                keep_going = False
            else:
                print('Name can not contain "BOT"!')

        print("Name set!")
        return name




if __name__ == '__main__':
    player = Player()
    name = player.select_name()
    print(name)
