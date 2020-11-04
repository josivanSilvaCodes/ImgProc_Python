import cv2 as cv
import numpy as np

img = cv.imread('brain_noisy.png')

kernel = np.array([
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5],
    [1/5, 1/5, 1/5, 1/5, 1/5]
    ])
#kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
imgs_concat = np.concatenate((img, dst), axis=1)

cv.imshow('brain_noisy',imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()
