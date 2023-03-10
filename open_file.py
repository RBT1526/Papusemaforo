import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("carros.jpg")
h, w, channels = img.shape
img = img[:,86:192]
h, w, channels = img.shape
half = w//2
left_part = img[:, :half]
img = cv2.cvtColor(left_part, cv2.COLOR_BGR2RGB)
cimg = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 30,100 )
cv2.imshow('Top', edges)
cv2.waitKey(0)
"""
half = w//2
left_part = img[:, :half]


img = cv2.cvtColor(left_part, cv2.COLOR_BGR2RGB)
# make a copy of the original image
cimg = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apply a blur using the median filter
img = cv2.medianBlur(img, 5)

circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9, 
                            minDist=80, param1=110, param2=39, maxRadius=70)
#print()

plt.imshow(img)
plt.show()
"""
"""
circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9, 
                            minDist=80, param1=110, param2=39, maxRadius=70)

for co, i in enumerate(circles[0, :], start=1):
    # draw the outer circle in green
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle in red
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
# print the number of circles detected
print("Number of circles detected:", co)
# save the image, convert to BGR to save with proper colors
# cv2.imwrite("coins_circles_detected.png", cimg)
# show the image
plt.imshow(cimg)
plt.show()
"""