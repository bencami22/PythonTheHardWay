from Zone import Zone
class Maze(Zone):
    def __init__(self):
        pass

    def play(self):
        while(True):
            print("Left or right?")
            user_input = input(">")
            if user_input == "left":
                return 'TreasureArea'
            elif user_input == "right":
                return 'DeathPit'
            else:
                print("Invalid input")
