import os,sys
import cv2
import numpy as np
import pytesseract
from PIL import Image


src_path =str(input('enter any working folder path: '))

def get_string(img_path):
    img = cv2.imread(input("enter image path: "))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(src_path + "removed.png", img)
    cv2.imwrite(src_path + "threshold.png", img)
    result = pytesseract.image_to_string(Image.open(src_path + "threshold.png"))
    

    return result


print ('--- Start recognize text from image ---')
print (get_string(src_path))

