import cv2
import numpy as np 

image = cv2.imread('tesla-model-s.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Hue, Saturation, Value
# [160, 100, 100], [179, 255, 255]
lower_red = np.array([160, 100, 100])
upper_red = np.array([179, 255, 255])
mask = cv2.inRange(image, lower_red, upper_red)

image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Tesla', cv2.cvtColor(image, cv2.COLOR_HSV2BGR))
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
    exit()