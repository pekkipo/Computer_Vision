import cv2
import numpy as np


# Load an image using 'imread' specifying the path to image
input_image = cv2.imread('./images/input.jpg')

# Our file 'input.jpg' is now loaded and stored in python
# as a varaible we named 'image'

# To display our image variable, we use 'imshow'
# The first parameter will be title shown on image window
# The second parameter is the image varialbe
cv2.imshow('Hello World', input_image)

# 'waitKey' allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open (time is in milliseconds here)
cv2.waitKey(0)

# This closes all open windows
# Failure to place this will cause your program to hang
cv2.destroyAllWindows()

print(input_image.shape)

# Print each dimension of the image

print('Height of Image:', int(input_image.shape[0]), 'pixels')
print('Width of Image: ', int(input_image.shape[1]), 'pixels')

# SAVE IMAGE
# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output.jpg', input_image)
cv2.imwrite('output.png', input_image)

