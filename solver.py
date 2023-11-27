# pylint: disable=all
# ^^^^^^
# This is for github enviroments, but I think I going to change to my normal Windows
# Yes, I use windows, someday I will change, but not now

# The data will be structured in a matrix with "x" and "y" axes predefined (size of the game),
# where the current state of the game will be stored.
# There will be another matrix to keep track of how many times a bomb has been placed in each position.

# Backtracking will be used to try all possible bomb positions but
# but a brute-force approach will be applied first.

# And then I will see what I do :)

# NUMBERS:
# 1-9: Minesweeper numbers
# 0: Empty spots
# A: Flag/Bomb
# B: To be discovered

# Also, I need to comment all the code


import numpy as np




class solver:
    def __init__(self):
        self.possibilities = 0
        map = ()
        self.define_map()
        self.bombs_location = []
        self.backtraking(self.map, self.remaining_bombs)
        
        
        
        shape = np.shape(self.map)
        
        for x in range(shape[0]):
            for y in range(shape[1]):
                self.probability_map[x,y] = self.probability_map[x,y] * 100 * self.remaining_bombs // self.possibilities 
                   
        
        print(self.possibilities)
        print(self.probability_map)
        
        
        
    
    def define_map(self):
        A = "A"
        B = "B"

        self.map = np.array((
            (A,2,A,1,0,0,0,0),
            (2,3,1,1,0,0,0,0),
            (A,1,0,0,0,0,0,0),
            (1,1,0,0,0,1,1,1),
            (0,0,1,2,3,3,A,1),
            (1,1,2,A,A,A,2,1),
            (B,B,2,B,B,B,B,B),
            (1,1,1,1,B,B,B,B)))
        
        self.probability_map = np.zeros(np.shape(self.map))
        
        self.remaining_bombs = 3
        
        
    def check_bomb(self, map):
    
        shape = np.shape(map)
        
        for x in range(shape[0]):
            for y in range(shape[1]):
                
                actual_cell = map[x][y]
                
                if actual_cell != "A" and actual_cell != "B" and actual_cell != "0":
                    
                    bombs = 0
                    
                    for xp in range(-1,2):
                        for yp in range(-1,2):
                            
                                xc = x + xp
                                yc = y + yp
                                
                                if xc >= 0 and xc <= shape[0] - 1 and yc >= 0 and yc <= shape[1] - 1:
                                    
                                    if map[xc][yc] == "A":
                                        bombs += 1

                            
                    if bombs != int(actual_cell):
                        return False
                    
        return True


    def backtraking(self, map, remaining_bombs):
        
        possible_bombs = np.argwhere(map == "B")
                    
        if remaining_bombs == 0:

            if self.check_bomb(map):
                self.possibilities += 1
                for i in range(len(self.bombs_location)):
                    
                    self.probability_map[self.bombs_location[i][0],self.bombs_location[i][1]] += 1
                    
                    return None
            else:
                return None
                
        else:
            for i in range(len(possible_bombs)):
                actual_map = map.copy()
                actual_remaining_bombs = remaining_bombs - 1
                actual_map[possible_bombs[i][0]][possible_bombs[i][1]] = "A"
                location_new_bomb = possible_bombs[i]
                self.bombs_location.append(location_new_bomb)
                self.backtraking(actual_map, actual_remaining_bombs)
                self.bombs_location.pop()
            return None
            



solver()


