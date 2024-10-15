# Instead of seen the screen(what is a torture), I going to simulate my own minsweeper

# The data will be structured in 2 matrices with "x" and "y" axes predefined (size of the game),
# the "final" is gona store all the bomb positions and numbers
# and the "actual" the current state of the game.

# NUMBERS:
# 1-9: Minesweeper numbers
# 0: Empty spots
# B: Bomb
# F: Flag
# U: To be discovered

import random

class Simulator:

    total_bombs = 0
    finalMap = []
    actualMap = []
    cells_pressed = []

    def __init__(self, sizex=10, sizey=10, total_bombs=5):
        self.total_bombs = total_bombs

        if(total_bombs >=sizex*sizey):
            raise Exception("Too many bombs, game is impossible")
        
        self.create_maps(sizex, sizey, total_bombs)
    
    # Create the maps
    def create_maps(self, sizex, sizey, total_bombs):

        self.finalMap = [[0 for j in range(sizex)] for i in range(sizey)]
        self.actualMap = [["U" for j in range(sizex)] for i in range(sizey)]

        for i in range(total_bombs):
            self.put_random_bomb(sizex, sizey)

        self.put_numbers(sizex, sizey)

    # Put the bombs when creating the maps
    def put_random_bomb(self, sizex, sizey):
        while True:
            x = random.randrange(sizex)
            y = random.randrange(sizey)
            if self.finalMap[y][x] == 0:
                self.finalMap[y][x] = "B"
                return

    # Put the numbers when creating the maps
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

    # Press the cell and if's 0 all the around it
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
    
    # Flag the cell
    def flag_cell(self, x, y):
        if self.actualMap[y][x] == "F":
            self.actualMap[y][x] = "U"
        else:
            self.actualMap[y][x] = "F"
        
    # See what is inside that cell
    def reveal_cell(self, x, y):
        self.actualMap[y][x] = self.finalMap[y][x]

    def get_bombs_remaining(self):
        count = 0
        for i in self.actualMap:
            for j in i:
                if j == "F":
                    count+=1
        return self.total_bombs - count
    
    def get_cells_to_finish(self):
        count = 0
        for i in self.actualMap:
            for j in i:
                if j == "U":
                    count+=1
        return count - self.get_bombs_remaining()

if __name__ == '__main__':
    Simulator(10, 10, 7)


