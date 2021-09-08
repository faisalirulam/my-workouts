import cv2
"""""
#gray scalle image read and show 
img = cv2.imread('gray_scale.jpg') 
cv2.imshow('sample image',img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

#black and white image read and show
img1 = cv2.imread('blackwhite.jpg')
cv2.imshow('sample',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

#color image read and show
img2 = cv2.imread('fyzl.jpg')
cv2.imshow('sample',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()