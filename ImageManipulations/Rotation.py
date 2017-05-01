# Rotation matrix:
# cos_phi  -sin_phi
# sin_phi  cos_phi
# phi - tha angle of rotation. anti-clock wise from central axis
# ps: roation phi angle bookmark

import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')
height, width = image.shape[:2]

# Divide by two to rototate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle of rotation, scale)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
# new width and new height of tha canvas to get rid of black surrounding should be actually calculated

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Other Option to Rotate
img = cv2.imread('../images/input.jpg')

rotated_image = cv2.transpose(img)
# already without black surrounding

cv2.imshow('Rotated Image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Horizontal flip.
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipped)
cv2.waitKey()
cv2.destroyAllWindows()