# Morphological operations

# Erosion - eliminates pixels at the boundaris of the object
# Dilation - adds pixels around the boundaries
# Important note: in fact erosion, for instance, will actually make a word thicker because the white pixels around the word would be considered
# to be belonging to the boundary of the word
# While dilation will make the word thiner. Bookmark: Dilation Erosion opposite effect
# That note would be applied when black characters on the white background


# Opening - erosion followed by dilation. Useful for getting rid of noise
# Closing - dilation followed by dilation

import cv2
import numpy as np

image = cv2.imread('../images/opencv_inv.png', 0)

cv2.imshow('Original', image)
cv2.waitKey(0)

# First define the kernel
# Let's define our kernel size
kernel = np.ones((5,5), np.uint8)

# Now we erode
erosion = cv2.erode(image, kernel, iterations = 1) # in most cases no need to run more than 1 iteration
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)

#
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)

# Opening - Good for removing noise
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)

# Closing - Good for removing noise
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)


cv2.destroyAllWindows()