import cv2
import numpy as np 

image = cv2.imread('tesla-model-s.jpg')

cv2.imshow('Tesla', image)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
    exit()