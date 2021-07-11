import cv2
import numpy as np 

image = cv2.imread('tesla-model-s.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# [160, 100, 100], [179, 255, 255]

cv2.imshow('Tesla', image)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
    exit()