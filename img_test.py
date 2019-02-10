import cv2
import numpy as np

import os

img  = cv2.imread('data/src/Berry.jpg')
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output/test.jpg", img)