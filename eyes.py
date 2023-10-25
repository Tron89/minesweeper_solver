
"""
import cv2

class process_image():

    def preprocess(not_preprocesed_image):
        gray = cv2.cvtColor(not_preprocessed_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh = cv2.threshold(blur, 170, 255, cv2.THRESH_BINARY_INV, cv2.THRESH_OTSU)[1] #cv2.THRESH_OTSU
        return thresh
    
if __name__ == '__main__':
    process_image()

"""

#no va por que lo ejecuta en servidor ruso, y no en esta patata :)