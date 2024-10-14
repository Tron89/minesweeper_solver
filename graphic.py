# This will be the graphic part of the program, where you gona play/see :)

# How this use Cartesian coordinates, and the others use Matrix coordinates,
# I created functions for the change.

import pyglet
from pyglet import shapes

class Graphic:

    def __init__(self, rows=10, cols=10, on_mouse_press=lambda x:print("Pressed"), update=lambda x:x, cell_size=25):
        self.window = pyglet.window.Window(rows*cell_size, cols*cell_size, "title")

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        # Create the cells
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]
        for col in range(cols):
            for row in range(rows):
                y = row * self.cell_size
                x = col * self.cell_size
                self.cells[row][col] = (shapes.Rectangle(x, y, self.cell_size-1, self.cell_size-1, color=(50, 50, 50)))

        # Create the cells numbers (inicialited in 0)
        self.numbers = [[0 for _ in range(cols)] for _ in range(rows)]

        # Pass the functions to pyglet 
        self.window.event(self.on_draw)
        self.window.event(self.on_key_press)
        self.window.event(on_mouse_press)

        # How often the update function is call
        pyglet.clock.schedule_interval(update, 1)

    # Draw all in the screen (I love puting unnecessary comments)
    def on_draw(self):
        self.window.clear()
        for row in self.cells:
            for cell in row:
                cell.draw()
        for row in self.numbers:
            for number in row:
                if number != 0:
                    number.draw()

    # It does nothing yet, it's just in case
    def on_key_press():
        pass

    # Get what cell represent that point of the screen
    def what_cell(self, x, y):
        col = x // self.cell_size 
        row = y // self.cell_size
        return self.cellPoint_to_matrixPoint(col, row)
    
    # Change the cell for the respectivly number (or flag)
    def change_cell(self, x, y, value, quit_cell):
        col, row = self.matrixPoint_to_cellsPoint(x, y)
        # Quit cell number if it has something
        if self.numbers[row][col] != 0:
            self.numbers[row][col].delete()
            self.numbers[row][col] = 0
        # Put de value in the cell
        else:
            if quit_cell:
                self.cells[row][col].color = (0, 0, 0)
            posx = col * self.cell_size
            posy = row * self.cell_size

            number = pyglet.text.Label(str(value),
                                    font_name='Arial', 
                                    font_size=self.cell_size-10, 
                                    color=(255, 255, 255),
                                    x=posx+10, 
                                    y=posy+10,
                                    anchor_x='center', anchor_y='center')
            if value != 0:
                self.numbers[row][col] = number

    def cellPoint_to_matrixPoint(self, col, row):
        x = col
        y = self.rows - (row  + 1)
        return x, y
    
    def matrixPoint_to_cellsPoint(self, x, y):
        col = x
        row = self.rows - y - 1
        return col, row


if __name__ == '__main__':
    Graphic()
    pyglet.app.run()
