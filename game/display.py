
class Display:
    
    def __init__(self):
        self.rules = ['1. Do not cheat', '2. Do not swear', '3. Do not fight', '4. Have fun']
    
    def display_rules(self):
        return self.rules
    
    def display_graphics(self,sentence):
        size = 20
        for row in range(size):
            if (row == 0) or (row == size-1):
                my_output = ("_"*(size*2))
                print(my_output)
            elif row == (size/2):
                print((sentence).center(size*2, '>'))
            elif (row % 2 == 0):
                print(' ' * (size+2))
    
    def display_highscore(self):
        """reads from txt file"""
        highscore_list = []
        HIGHSCORE_FILE = 'C:/Users/David Trang/Ass2Game/sus_prog_game/game/highscores.txt'
        with open(HIGHSCORE_FILE, 'r') as highscore_file:
            for line in highscore_file:
                name, score = line.split(':')
                highscore_list.append((name, int(score)))
        highscore_list = sorted(highscore_list)
        highscore_file.close
        
        """loops each highscore on the list"""
        displayer = Display()
        counter = 1
        for name, score in highscore_list:
            displayer.display_graphics((f' Number.{counter} {name} --> {score} Rolls'))
            counter += 1
    

        
if __name__ == '__main__':
    displayer = Display()
    displayer.display_highscore()
    