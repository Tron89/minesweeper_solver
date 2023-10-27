# pylint: disable=all


import numpy as np


solution = (
    (0,0,0,0,1,"A",1,0),
    (0,0,0,0,1,1,1,0),
    (1,1,1,0,1,2,2,1),
    (1,"A",2,1,1,"A","A",1),
    (1,2,"A",1,1,3,"B","B"),
    (1,2,2,1,0,1,"A","A"),
    ("B","A",1,0,0,1,4,"A"),
    ("B",1,1,0,0,0,2,"A"))

solution = np.array(solution)

def check_bomb(map):

    shape = np.shape(map)
    for x in range(shape[0]):
        for y in range(shape[1]):
            
            actual_cell = map[x][y]
            
            if actual_cell != "A" and actual_cell != "B" and actual_cell != "0":
                print("actual cell: ",actual_cell)
                
                bombs = 0
                
                for xp in range(-1,2):
                    for yp in range(-1,2):
                        
                            xc = x + xp
                            yc = y + yp

                            if xc >= 0 and xc <= shape[0] - 1 and yc >= 0 and yc <= shape[1] - 1:
                                if map[xc][yc] == "A":
                                    print("si hay bomba")
                                    bombs += 1
   
                if bombs != int(actual_cell):
                    return False
                
    return True


if check_bomb(solution):
    print("si va")
else:
    print("no va :(")