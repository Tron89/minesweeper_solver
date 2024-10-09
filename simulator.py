# Instead of seen the screen(what is a torture), I going to simulate my own minsweeper

# The data will be structured in 2 matrices with "x" and "y" axes predefined (size of the game),
# the first si gona store all the bomb positions
# and the second the current state of the game.

# NUMBERS:
# 1-9: Minesweeper numbers
# 0: Empty spots
# B: Bomb
# F: Flag
# U: To be discovered

# Also, I need to comment all the code

import random

class Simulator:

    total_bombs = 0
    finalMap = []
    actualMap = []
    cells_pressed = []

    def __init__(self, sizex, sizey, total_bombs):
        self.total_bombs = total_bombs

        if(total_bombs >=sizex*sizey):
            raise Exception("Too many bombs, game is impossible")
        
        self.create_maps(sizex, sizey, total_bombs)

        for i in self.finalMap:
            print(i)



        """
        for i in self.finalMap:
            print(i)
        print("-------------------")
        for i in self.actualMap:
            print(i)

        while(True):
            x = int(input("Elige x para pulsar: "))
            y = int(input("Elige y para pulsar: "))

            if(self.press_cell(x, y) == "BOOM!"):
                break

            for i in self.finalMap:
                print(i)
            print("-------------------")
            for i in self.actualMap:
                print(i)
        """
    
    def create_maps(self, sizex, sizey, total_bombs):

        self.finalMap = [[0 for j in range(sizex)] for i in range(sizey)]
        self.actualMap = [["U" for j in range(sizex)] for i in range(sizey)]

        for i in range(total_bombs):
            self.put_random_bomb(sizex, sizey)

        self.put_numbers(sizex, sizey)


    def put_random_bomb(self, sizex, sizey):
        while True:
            x = random.randrange(sizex)
            y = random.randrange(sizey)
            if self.finalMap[y][x] == 0:
                self.finalMap[y][x] = "B"
                return


    def press_cell(self, x, y, first):
        if (y < len(self.finalMap) and y >= 0 and x < len(self.finalMap[y]) and x >= 0 and self.actualMap[y][x] == "U"):
            if self.finalMap[y][x] == "B":
                return "BOOM!"
            elif self.finalMap[y][x] == 0:
                self.reveal_cell(x, y)
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        self.press_cell(x+i, y+j, False)
                self.cells_pressed.append((x, y, self.finalMap[y][x]))
                if (first):
                    cells_pressed = self.cells_pressed
                    self.cells_pressed = []
                    return cells_pressed
            else:
                self.reveal_cell(x, y)
                self.cells_pressed.append((x, y, self.finalMap[y][x]))
                if(first):
                    cells_pressed = self.cells_pressed
                    self.cells_pressed = []
                    return cells_pressed
                return
            
    def flag_cell(self, x, y):
        if self.actualMap[y][x] == "F":
            self.actualMap[y][x] = "U"
        else:
            self.actualMap[y][x] = "F"
        

    def reveal_cell(self, x, y):
        self.actualMap[y][x] = self.finalMap[y][x]


    def put_numbers(self, sizex, sizey):

        for y in range(sizey):
            for x in range(sizex):
                if self.finalMap[y][x] == 0:
                    count = 0
                    for yt in range(-1, 2):
                        for xt in range(-1, 2):
                            if y+yt >= 0 and y+yt < sizey and x+xt >= 0 and x+xt < sizex:                                
                                if self.finalMap[y+yt][x+xt] == "B":
                                    count += 1
                    self.finalMap[y][x] = count



if __name__ == '__main__':
    Simulator(10, 10, 7)


