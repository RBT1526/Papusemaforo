import cv2
 
img = cv2.imread('carros.jpg')
 
# cv2.imread() -> takes an image as an input
h, w, channels = img.shape
 
half = w//2
 
 
# this will be the first column
left_part = img[:, :half]
 
# [:,:half] means all the rows and
# all the columns upto index half
 
# this will be the second column
right_part = img[:, half:] 
 
# [:,half:] means all the rows and all
# the columns from index half to the end
# cv2.imshow is used for displaying the image
cv2.imshow('Left part', left_part)
cv2.imshow('Right part', right_part)
cv2.waitKey(0)
# this is horizontal division
half2 = h//2
 
top = img[:half2, :]
bottom = img[half2:, :]
 
cv2.imshow('Top', top)
cv2.imshow('Bottom', bottom)