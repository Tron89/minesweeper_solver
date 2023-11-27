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

        preprocessed = self.preprocess(screenshot)
        # HACK: Temporaly for a good debug :D
        # I have to do a error handling
        cv2.imshow("tresh image",preprocessed)

        location_minesweeper = self.find_minesweeper(preprocessed)

        # HACK: Also for a good debug :D
        screenshot = np.array(screenshot)
        cv2.drawContours(screenshot, [location_minesweeper], -1, (0,255,0), 3)
        cv2.imshow("b",screenshot)
        cv2.waitKey(0)


    # Search for the location of the minesweeper
    def find_minesweeper(self, preprocessed):
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

                # And it does it 
                final_contour = np.array([coord_min_xy, coord_min_y, coord_max_xy, coord_min_x], dtype=np.int32)
                final_contour = final_contour.reshape((-1, 1, 2))

                return final_contour




    # Preprocess the image to a better search
    def preprocess(self, not_preprocessed_image):
        gray = cv2.cvtColor(np.array(not_preprocessed_image), cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.threshold(blur, 170, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)[1]
        return thresh
    


if __name__ == '__main__':
    process_image()