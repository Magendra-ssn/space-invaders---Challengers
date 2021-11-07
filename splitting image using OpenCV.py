import cv2
import numpy as np
img = cv2.imread("foo.jpg")
b,g,r = cv2.split(img)