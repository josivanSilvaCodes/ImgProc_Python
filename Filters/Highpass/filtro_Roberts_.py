import cv2 as cv
import numpy as np

img = cv.imread('taj_noise.jpg')

kernel_Roberts_x = np.array([
    [1, 0],
    [0, -1]
    ])

dst = cv.filter2D(img,-1,kernel_Roberts_x)

imgs_concat = np.concatenate((img, dst), axis=1)

cv.imshow('taj_noise',imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()



