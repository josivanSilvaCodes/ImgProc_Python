import cv2
 
image = cv2.imread('Lena_noisy.png')
gaussian_blur = cv2.GaussianBlur(image,(5,5),sigmaX=0)
edges = cv2.Canny(gaussian_blur,100,200)
 
cv2.imshow('Noisy image', image)
cv2.imshow('Edges image', edges)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
