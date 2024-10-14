# This will conect all the modules into a incredible and magnific frankestain

from simulator import Simulator
from graphic import Graphic
from solver import Solver
import pyglet
import numpy as np

def exit_game():
    exit("Ja, perdistes :)")

# When you press the cell it find what cell it is, put it in the simulator en then in the graphic
def on_mouse_press(x, y, button, modifiers):

    # Verify what cell is presed and display or lose depending on what is in that cell
    if button == pyglet.window.mouse.LEFT:
        x, y = graphic.what_cell(x, y)
        values = simulator.press_cell(x, y, True)
        if values == "BOOM!":
            exit_game()
        for i in values:
            graphic.change_cell(i[0], i[1], i[2], True)

    # Put/quit a flag of a cell
    if button == pyglet.window.mouse.RIGHT:
        x, y = graphic.what_cell(x, y)
        simulator.flag_cell(x, y)
        graphic.change_cell(x, y, "F", False)


def update(dt):

    # Calculate the cells necesary to finish the map
    remaining_bombs = bombs - np.count_nonzero(np.array(simulator.actualMap) == "F")
    solver.backtraking(simulator.actualMap, remaining_bombs)
    cells_to_finish = np.count_nonzero(np.array(simulator.actualMap) == "U") - remaining_bombs

    # If there are still cells to finish get the min posibility of bomb cell
    if cells_to_finish != 0:
        y, x = solver.get_min(simulator.actualMap)

        values = simulator.press_cell(x, y, True)
        if values == "BOOM!":
            exit_game()
        for i in values:
            graphic.change_cell(i[0], i[1], i[2], True)


sizex = 5
sizey = 5
bombs = 3

simulator = Simulator(sizex, sizey, bombs)

graphic = Graphic(sizex, sizey, on_mouse_press, update, 20)

solver = Solver(simulator.actualMap)

pyglet.app.run()