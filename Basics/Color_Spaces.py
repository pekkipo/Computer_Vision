# RGB, CMYK, HSV - hue saturation value (brightness)

# hsv is useful for color segmentation

import cv2
import numpy as np

image = cv2.imread('./images/input.jpg')

# BGR Values for the 10,50 pixel
B, G, R = image[10, 50]
print B, G, R
print image.shape
#13 19 32
#(830L, 1245L, 3L)

# cvt - convert
# Convert to gray scalse
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print gray_img.shape
print gray_img[10, 50]

#(830L, 1245L) now 2 dims with one 0-255 value
#22

# HSV
#H: 0 - 180, S: 0 - 255, V: 0 - 255


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])  # :  :   all values of 1st and 2nd dimensions (w, h)
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()


# Explore individual channels in RGB

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

print B.shape
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()
# that above will actually give gray scale images

# Let's re-make the original image (rgb)
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# Let's amplify the blue color, add 100 to every value in a blue channel
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Now see rgb channels not in a gray scale
B, G, R = cv2.split(image)

# Let's create a matrix of zeros
# with dimensions of the image h x w
zeros = np.zeros(image.shape[:2], dtype = "uint8")
# zeros 830 x 1245

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()

