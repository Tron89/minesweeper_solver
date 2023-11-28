# TODO: Finish it :D
# It only catch where is the minesweeper, it has to detect all there is in
# I also have to change some values to detect well the minesweeper :)
# (now is terrible at it)

import cv2
import pyautogui
import numpy as np

class process_image():

    def __init__(self):
        # Take a screenshot and find the sudoku
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)

        preprocessed = self.preprocess(screenshot)
        # HACK: Temporaly for a good debug :D
        # I have to do a error handling
        cv2.imshow("tresh image",preprocessed)

        minesweeper = self.find_minesweeper(preprocessed, screenshot)
        # HACK: Also for a good debug :D
        cv2.imshow("minesweeper",minesweeper)
        
        # This will divide the minesweeper into parts(number of bombs...)
        a, b, c = self.detect_from_minesweeper()
        cv2.waitKey(0)

    def detect_from_minesweeper(self):
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
                minesweeper = screenshot[coord_min_xy[1]:coord_max_xy[1], coord_min_xy[0]:coord_max_xy[0]]

                return minesweeper




    # Preprocess the image to a better search
    def preprocess(self, not_preprocessed_image):
        gray = cv2.cvtColor(np.array(not_preprocessed_image), cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.threshold(blur, 170, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)[1]
        return thresh
    


if __name__ == '__main__':
    process_image()