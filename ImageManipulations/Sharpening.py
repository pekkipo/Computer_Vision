# By altering our kernels one can implement sharpening, which has the effects of in strengthening or emphasizing edges in an image.
# opposite of blurring
# pay attention to the kernel matrix filled with -1 and 9 in the center
# the sum of the matrix must be equal 1. 9-8 = 1
# since sums to 1 there is no need to normalize it

import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')
cv2.imshow('Original', image)

# Create our shapening kernel, we don't normalize since the
# the values in the matrix sum to 1
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

# applying different kernels to the input image
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

cv2.imshow('Image Sharpening', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()