# Where I will conect all the modules into a incredible and magnific frankestain

from simulator import Simulator
from graphic import Graphic
from solver import Solver
import pyglet
import numpy as np


def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        x, y = graphic.what_cell(x, y)
        values = simulator.press_cell(x, y, True)
        if values == "BOOM!":
            print("ja, perdistes :)")
            graphic.close_window()
            exit("Ja, perdistes")
        for i in values:
            graphic.change_cell(i[0], i[1], i[2], True)

    if button == pyglet.window.mouse.RIGHT:
        x, y = graphic.what_cell(x, y)
        simulator.flag_cell(x, y)
        graphic.change_cell(x, y, "F", False)

def update(dt):
    remaining_bombs = bombs - np.count_nonzero(np.array(simulator.actualMap) == "F")
    solver.backtraking(simulator.actualMap, remaining_bombs)

    cells_to_finish = np.count_nonzero(np.array(simulator.actualMap) == "U") - remaining_bombs

    if cells_to_finish != 0:
        #print(solver.probability_map)
        y, x = solver.get_min(simulator.actualMap)
        #print("aaaa: ", x, y)
        solver.flush()

        values = simulator.press_cell(x, y, True)
        if values == "BOOM!":
            print("ja, perdistes :)")
            graphic.close_window()
            exit("Ja, perdistes")
        for i in values:
            graphic.change_cell(i[0], i[1], i[2], True)
    
    # x, y = graphic.what_cell(x, y)
    # values = simulator.press_cell(x, y, True)
    # if values == "BOOM!":
    #     print("ja, perdistes :)")
    #     graphic.close_window()
    #     exit("Ja, perdistes")
    # for i in values:
    #     graphic.change_cell(i[0], i[1], i[2], True)


sizex = 5
sizey = 5
bombs = 5

simulator = Simulator(sizex, sizey, bombs)

graphic = Graphic(sizex, sizey, 20, on_mouse_press, update)

solver = Solver(simulator.actualMap)

pyglet.app.run()