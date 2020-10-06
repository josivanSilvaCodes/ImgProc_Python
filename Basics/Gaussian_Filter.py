import cv2
 
image = cv2.imread('Lena_noisy.png')
gaussian_blur = cv2.GaussianBlur(image,(11,11),sigmaX=0)
 
cv2.imshow('Noisy image', image)
cv2.imshow('Smooth image', gaussian_blur)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
