import cv2
import numpy as np

img = cv2.imread('brain_noisy.png')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1) 

cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows




