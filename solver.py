# The data will be structured in a matrix with "x" and "y" axes predefined (size of the game),
# where the current state of the game will be stored.
# There will be another matrix to keep track of how many times a bomb has been placed in each position.

# Backtracking will be used to try all possible bomb positions with
# with a brute-force approach.

# NUMBERS:
# 1-9: Minesweeper numbers
# 0: Empty spots
# F: Flag/Bomb
# U: To be discovered

# TODO: Change to a better backtracking technique

import copy

class Solver:
    
    # For the backtracking
    bombs_location = []
    # To see in probability how posible is that there is a bomb 
    possibilities = 0


    def __init__(self, map):
        self.probability_map = [[0 for i in map[0]] for i in map]


    # Verify if it's posible that display
    def check_bomb(self, map):
        
        for y in range(len(map)):
            for x in range(len(map[0])):
                
                actual_cell = map[x][y]
                
                if actual_cell != "F" and actual_cell != "U" and actual_cell != 0:
                    
                    bombs = 0
                    
                    for xp in range(-1,2):
                        for yp in range(-1,2):
                                
                                xc = x + xp
                                yc = y + yp
                                
                                if xc >= 0 and xc <= len(map) - 1 and yc >= 0 and yc <= len(map[0]) - 1:
                                    
                                    if map[xc][yc] == "F":
                                        bombs += 1

                    if bombs != int(actual_cell):
                        return False
        return True

    # The main function where all the magic happens :)
    # It will try all possible bomb positions, calling himself
    def backtraking(self, map, remaining_bombs, points = 0):

        # Find the undefined cells
        possible_bombs = [(i, j) for i, row in enumerate(map) for j, value in enumerate(row) if value == "U"]

        # If there are no bombs to put, add the posibilities to the posibility map and go back
        if remaining_bombs == 0:
            if self.check_bomb(map):
                self.possibilities += 1
                for i in range(len(self.bombs_location)):
                    self.probability_map[self.bombs_location[i][0]][self.bombs_location[i][1]] += 1
                    
                return None
            else:
                return None
        
        # If there are bombs go forward to the next backtraking function
        else:
            next_point = points
            for i in range(points, len(possible_bombs)):
                actual_map = copy.deepcopy(map)
                actual_remaining_bombs = remaining_bombs - 1
                actual_map[possible_bombs[i][0]][possible_bombs[i][1]] = "F"
                location_new_bomb = possible_bombs[i]
                self.bombs_location.append(location_new_bomb)
                self.backtraking(actual_map, actual_remaining_bombs, next_point)
                self.bombs_location.pop()
                next_point += 1
            return None


    def get_min(self, map, remaining_bombs):
        # Prepare all
        self.probability_map = [[0 for i in map[0]] for i in map]
        self.possibilities = 0

        # Do the backtraking 
        self.backtraking(map, remaining_bombs)

        # Search the min

        # Now it's with percentages
        self.probability_map = [[j/self.possibilities for j in self.probability_map[i]] for i in range(len(self.probability_map))]
        
        # Find the minimum probability cell
        possible_bombs_location = [(i, j) for i, row in enumerate(map) for j, value in enumerate(row) if value == "U"]
        possible_bombs_probability = [self.probability_map[possible_bombs_location[i][0]][possible_bombs_location[i][1]] for i in range(len(possible_bombs_location))]
        minimum = min(possible_bombs_probability)
        return possible_bombs_location[possible_bombs_probability.index(minimum)]


if __name__ == '__main__':

    F = "F"
    U = "U"

    map = [
        [F,2,F,1,0,0,0,0],
        [2,3,1,1,0,0,0,0],
        [F,1,0,0,0,0,0,0],
        [1,1,0,0,0,1,1,1],
        [0,0,1,2,3,3,F,1],
        [1,1,2,F,F,F,2,1],
        [1,U,2,U,U,U,U,U],
        [1,1,1,1,U,U,U,U]]
    
    bombs = 3

    solver = Solver(map)

    solver.get_min(map, bombs)
    for i in solver.probability_map:
        print(i)




