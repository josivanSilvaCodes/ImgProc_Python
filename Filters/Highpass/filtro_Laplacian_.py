import cv2 as cv
import numpy as np

img = cv.imread('taj_noise.jpg')

kernel_Laplacian = np.array([
    [1,  1,  1],
    [1, -8,  1],
    [1,  1,  1]])

dst = cv.filter2D(img,-1,kernel_Laplacian)

imgs_concat = np.concatenate((img, dst), axis=1)

cv.imshow('taj_noise',imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()
