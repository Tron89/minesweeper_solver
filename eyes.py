# TODO: Finish it :D
# It only catch where is the minesweeper, it has to detect all there is in
# I also have to change some values to detect well the minesweeper :)
# (now is terrible at it)

import cv2
import pyautogui
import numpy as np

class process_image():

    # This values are for save where are the things
    pixels_to_minesweeper = []
    pixels_to_game = []
    pixels_to_time_counter = []
    pixels_to_mines_counter = []

    def __init__(self):
        # Take a screenshot and find the sudoku
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)

        preprocessed = self.preprocess(screenshot, 170)
        # HACK: Temporaly for a good debug :D
        # I have to do a error handling
        cv2.imshow("tresh image",preprocessed)

        minesweeper = self.find_minesweeper(preprocessed, screenshot)
        # HACK: Also for a good debug :D
        cv2.imshow("minesweeper",minesweeper)
        
        # This will divide the minesweeper into parts(number of bombs...)
        a, b, c = self.detect_from_minesweeper(minesweeper)
        cv2.waitKey(0)

    # HACK: All this have horrible names, I may sove it
    def detect_from_minesweeper(self, minesweeper):

        # Find the counter of mines and time :)
        def counters(minesweeper):
            save = []
            minesweeper_preproccesed = self.preprocess(minesweeper, 130)
            contours, _ = cv2.findContours(minesweeper_preproccesed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
            cv2.imshow("counters preprocesed minesweeper", minesweeper_preproccesed)
            
            for i, contour in enumerate(contours):
                epsilon = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.01 * epsilon, True)
                # It get all it is a quadrilateral decently large
                if len(approx) == 4 and epsilon >= 100:
                    save.append(contour)

            # HACK: More for a good debug :)
            cv2.drawContours(minesweeper, save, -1, (0,255,0), 3)
            cv2.imshow("contour minesweeper", minesweeper)
            return save[0], save[1]
        
        # The width and it's position
        def game_location(minesweeper):
            savex = []
            savey = []
            minesweeper_preproccesed = self.preprocess(minesweeper, 150)
            contours, _ = cv2.findContours(minesweeper_preproccesed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
            # HACK
            cv2.imshow("game preprocesed minesweeper", minesweeper_preproccesed)
            
            # Get the first value and he is the max y objective
            # The first should be the first right-down cell

            # And gets the last line of the minseweeper

            first = contours[0]
            epsilon = cv2.arcLength(first, True)
            approx = cv2.approxPolyDP(first, 0.01 * epsilon, True)
            
            max_y_first = np.argmin(approx[:, :, 1])
            coord_max_y_first = approx[max_y_first][0][1]
            epsilon_aprox = epsilon
            
            for i, contour in enumerate(contours):
                epsilon = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.01 * epsilon, True)
            
                max_y = np.argmin(approx[:, :, 1])
                coord_max_y = approx[max_y][0][1]
                
                # It get if is arround the first value max
                if coord_max_y >= coord_max_y_first - 5 and coord_max_y <= coord_max_y_first + 5 and epsilon >= epsilon_aprox - 5 and epsilon <= epsilon_aprox + 5:
                    savex.append(contour)
            
            # The max x of the last line
            # Whith that it gets the last column

            # Joints all the contours
            all_savex = np.concatenate(savex, axis=0)
        
            max_x_last = np.argmax(all_savex[:, :, 0])
            coord_max_x_last = all_savex[max_x_last][0][0]

            for i, contour in enumerate(contours):

                epsilon = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.01 * epsilon, True)
                
                max_x = np.argmax(approx[:, :, 0])
                coord_max_x = approx[max_x][0][0]
                
                if coord_max_x >= coord_max_x_last - 5 and coord_max_x <= coord_max_x_last + 5 and epsilon >= epsilon_aprox - 5 and epsilon <= epsilon_aprox + 5:
                    savey.append(contour)

            
            borders_cells = np.concatenate(savex + savey, axis=0)
            
            max_xy = np.argmax(borders_cells[:, :, 0] + borders_cells[:, :, 1])
            coord_max_xy = borders_cells[max_xy][0]

            min_x = np.argmin(borders_cells[:, :, 0])
            coord_min_x = borders_cells[min_x][0]

            min_y = np.argmin(borders_cells[:, :, 1])
            coord_min_y = borders_cells[min_y][0]

            coord_min_xy = [coord_min_x[0], coord_min_y[1]]
            
            game = minesweeper[coord_min_xy[1]:coord_max_xy[1], coord_min_xy[0]:coord_max_xy[0]]
            
            self.pixels_to_game = [self.pixels_to_game[0] + coord_min_xy[1], self.pixels_to_game[0] + coord_max_xy[1], self.pixels_to_game[2] + coord_min_xy[0], self.pixels_to_game[2] + coord_max_xy[0]]
            print("pixels", self.pixels_to_game)
            
            # HACK
            cv2.imshow("game screen", game)

            
            width = len(savex)
            height = len(savey)

            game_data = {
                "width" : width,
                "height" : height,
                "game_screen" : game,
                "croppedX" : (coord_min_xy[0],coord_max_xy[0]),
                "cropedY" : (coord_min_xy[1],coord_max_xy[1])

            }

            # HACK
            cv2.drawContours(game_part, savex, -1, (0,255,0), 3)
            cv2.drawContours(game_part, savey, -1, (0,255,0), 3)
            cv2.imshow("borders minesweeper", game_part)
            
            return game_data
            



        # Main function
        time_counter, mines_counter = counters(minesweeper.copy())
        
        max_y = np.argmax(mines_counter[:, :, 1])
        coord_max_y = mines_counter[max_y][0][1]

        game_part = minesweeper.copy()[coord_max_y + 5:,:]

        self.pixels_to_game = [coord_max_y + 5, 0, 0, 0]

        game_data = game_location(game_part)

        a = 1
        b = 2
        c = 3
        
        return a, b, c

    # Search for the location of the minesweeper
    def find_minesweeper(self, preprocessed, screenshot):
        # Find external contours
        contours, _ = cv2.findContours(preprocessed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]

        for contour in contours:

            # Takes the area of the contour
            epsilon = cv2.arcLength(contour, True)
            # And it approximates the vertices
            approx = cv2.approxPolyDP(contour, 0.01 * epsilon, True)
            
            # HACK: It see the number of sides and the size, probably is going to bring to an error, but for now is fine :)
            if len(approx) <= 4 and epsilon >= 900:

                # Takes the values to do a good quadrilateral :)
                max_xy = np.argmax(approx[:, :, 0] + approx[:, :, 1])
                coord_max_xy = approx[max_xy][0]

                min_x = np.argmin(approx[:, :, 0])
                coord_min_x = approx[min_x][0]

                min_y = np.argmin(approx[:, :, 1])
                coord_min_y = approx[min_y][0]

                coord_min_xy = [coord_min_x[0], coord_min_y[1]]

                # And it crops that part to simplify the rest of the code
                # It subtract some pixels to remove the sides
                minesweeper = screenshot[coord_min_xy[1]+5:coord_max_xy[1]-5, coord_min_xy[0]+5:coord_max_xy[0]-5]
                self.pixels_to_minesweeper = [coord_min_xy[1]+5, coord_max_xy[1]-5, coord_min_xy[0]+5, coord_max_xy[0]-5]

                return minesweeper




    # Preprocess the image to a better search
    def preprocess(self, not_preprocessed_image, threshold):
        gray = cv2.cvtColor(np.array(not_preprocessed_image), cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)[1]
        return thresh
    


if __name__ == '__main__':
    process_image()