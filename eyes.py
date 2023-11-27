# pylint: disable=all

import cv2
import pyautogui
import numpy as np

class process_image:

    def __init__(self):
        pyautogui.hotkey("alt", "tab", interval=0.1)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        image = self.preprocess(image)
        contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        print(contours)
        cv2.drawContours(image, contours, 10, (0,255,0))
        cv2.imshow("image",image)
        cv2.waitKey(0)
        
    def preprocess(self, not_preprocessed_image):
        gray = cv2.cvtColor(not_preprocessed_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)[1] #cv2.THRESH_OTSU
        return thresh
    


if __name__ == '__main__':
    process_image()