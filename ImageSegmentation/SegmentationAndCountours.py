
import cv2
import numpy as np

# Let's load a simple image with 3 black squares
# image = cv2.imread('../images/shapes.jpg')
image = cv2.imread('../images/shapes_donut.jpg')
cv2.imshow('Input Image', image)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), since findContours alters the image
_, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# findCountpurs(image, retrieval mode, approximation mode)
# retrieval modes are explained at Retrieval Modes bookmark. RETR_EXT seems to be the most general one to use
# hierarchy will return next, first child and a parent. Google more

# Important! If need only external contours - use RETR_EXTERNAL
# But if change the file to shapes with holes so to say, lika a donut - then we need also inner contours
# to achieve that change retrieval mode to RETR_LIST
# RETR all or tree will help to determine the layers also

cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

# In OpenCV 3.X, findContours returns a 3rd argument which is ret (or a boolean indicating if the function was successfully run).
# So replace line 20 with:
# _, contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# The variable 'contours' are stored as a numpy array of (x,y) points that form the contour
# While, 'hierarchy' describes the child-parent relationships between contours (i.e. contours within contours)
print(contours)  # prints coordinates of contours
# OpenCV stores contours as a list of lists
print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# Use '-1' as the 3rd parameter to draw all
cv2.drawContours(image, contours, -1, (0,255,0), 3) # 0 255 0 - green

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()