import cv2
import numpy as np

img = cv2.imread('brain_noisy.png')

blur1 = cv2.blur(img,(3,3))
blur2 = cv2.blur(blur1,(3,3))
blur3 = cv2.blur(blur2,(3,3))

compare = np.concatenate((img, blur3), axis=1) 

cv2.imshow('img', compare)
cv2.waitKey(0)
cv2.destroyAllWindows




