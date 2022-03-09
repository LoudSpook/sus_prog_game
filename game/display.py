
class Display:
    
    def __init__(self):
        self.rules = ['1. Do not cheat', '2. Do not swear', '3. Do not fight', '4. Have fun']
    
    def display_rules(self):
        return self.rules
    
    def display_graphics(self):
        size = 11
        sentence = "This is my sentence"
        for row in range(size):
            if (row == 0) or (row == size-1):
                my_output = ("_"*(len(sentence)*2))
                print(my_output)
            elif row == ((size-1)/2):
                print(sentence.center(len(sentence)*2, '>'))
            else:
                print(' ' * (size+2))

        
        
    

if __name__ == '__main__':
    displayer = Display()
    print(displayer.display_rules())
    print(displayer.display_graphics())
    