#Number plate detector

import cv2
import matplotlib.pyplot as plt
import numpy as np

BGR_im = cv2.imread("Vehicleno.jpg",1)#BGR
HSV_im = cv2.cvtColor(BGR_im,cv2.COLOR_BGR2HSV)

Blue_UB = np.array([50,255,255])#HSV
Blue_LB = np.array([20,50,200])

mask = cv2.inRange(HSV_im,Blue_LB,Blue_UB)

cv2.namedWindow("BGR Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Mask Image", cv2.WINDOW_NORMAL)
cv2.imshow("BGR Image", BGR_im)
cv2.imshow("Mask Image", mask)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
