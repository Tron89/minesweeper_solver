# This will be the graphic part of the program, where you gona play :)

import pyglet
from pyglet import shapes

class Graphic:

    def __init__(self, rows, cols, cell_size, on_mouse, update):
        self.window = pyglet.window.Window(rows*cell_size, cols*cell_size, "title")

        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

        
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]
        for col in range(cols):
            for row in range(rows):
                y = row * self.cell_size
                x = col * self.cell_size
                self.cells[row][col] = (shapes.Rectangle(x, y, self.cell_size-1, self.cell_size-1, color=(50, 50, 50)))

        self.numbers = [[0 for _ in range(cols)] for _ in range(rows)]

        self.window.event(self.on_draw)
        self.window.event(self.on_key_press)
        self.window.event(on_mouse)

        pyglet.clock.schedule_interval(update, 1)


    def on_draw(self):
        self.window.clear()
        for row in self.cells:
            for cell in row:
                cell.draw()
        for row in self.numbers:
            for number in row:
                if number != 0:
                    number.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        col = x // self.cell_size
        row = y // self.cell_size
        print(f"Clic en celda: ({row}, {col})")
        self.cells[row][col].color = (100, 100, 100)

    def what_cell(self, x, y):
        col = x // self.cell_size 
        row = y // self.cell_size
        return self.cellPoint_to_matrixPoint(col, row)
    
    def cellPoint_to_matrixPoint(self, col, row):
        x = col
        y = self.rows - (row  + 1)
        return x, y
        
    def matrixPoint_to_cellsPoint(self, x, y):
        col = x
        row = self.rows - y - 1
        return col, row
    
    def change_cell(self, x, y, value, color):
        col, row = self.matrixPoint_to_cellsPoint(x, y)
        if self.numbers[row][col] != 0:
            self.numbers[row][col].delete()
            self.numbers[row][col] = 0
        else:
            if color:
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

    
    def on_key_press(self, symbol, modifiers):
        pass

    def update(self, dt):
        pass

    def close_window(self):
        self.window.close()


if __name__ == '__main__':
    rows = 10
    cols = 10
    cell_size = 20

    mi_ventana = Graphic(10, 10, 20)

    pyglet.app.run()













#  # This will be the graphic part of the program, where you gona play :)

# import pyglet

# class Graphic:
#     def __init__(self, width, height, rows, cols, cell_size):
#         self.window = pyglet.window.Window(width, height, "title")
        
#         self.label = pyglet.text.Label('¡Hola, Pyglet!', 
#                                        font_name='Times New Roman', 
#                                        font_size=36, 
#                                        x=self.window.width // 2, 
#                                        y=self.window.height // 2,
#                                        anchor_x='center', anchor_y='center')

#         self.image = pyglet.resource.image('mi_imagen.jpg')

#         self.image = self.resize_image(self.image, 100)

#         self.x = 100
#         self.y = 100

#         self.window.event(self.on_draw)
#         self.window.event(self.on_key_press)

#         pyglet.clock.schedule_interval(self.update, 1 / 60.0)

#     def resize_image(self, image, new_width):
#         scale_factor = new_width / image.width
#         image.width = new_width
#         image.height = int(image.height * scale_factor)
#         return image

#     def on_draw(self):
#         self.window.clear()
#         self.label.draw()
#         self.image.blit(self.x, self.y)

#     def on_key_press(self, symbol, modifiers):
#         if symbol == pyglet.window.key.LEFT:
#             self.x -= 10
#         elif symbol == pyglet.window.key.RIGHT:
#             self.x += 10

#     def update(self, dt):
#         self.x += 100 * dt
#         if self.x > self.window.width:
#             self.x = 0


# if __name__ == '__main__':

#     mi_ventana = Graphic(640, 480, 10, 10, 5)

#     pyglet.app.run()


