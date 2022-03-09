
class Display:
    
    def __init__(self):
        self.rules = ['1. Do not cheat', '2. Do not swear', '3. Do not fight', '4. Have fun']
    
    def display_rules(self):
        return self.rules
    

if __name__ == '__main__':
    displayer = Display()
    print(displayer.display_rules())
    