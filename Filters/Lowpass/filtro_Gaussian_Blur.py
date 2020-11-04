import cv2
import numpy as np

img = cv2.imread('brain_noisy.png')
Gauss = cv2.GaussianBlur(img,(5,5),0)
compare = np.concatenate((img, Gauss), axis=1) 

cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows




