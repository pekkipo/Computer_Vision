# Blobs are groups of connected pixels that share a common property

# OpenCV's simpleBlobDetector
# Create detector - input image into detector - obtain key points - draw key points


import cv2
import numpy as np

# Read image
#image = cv2.imread("../images/Sunflowers.jpg")
# better seen on a grayscale image
image = cv2.imread("../images/Sunflowers.jpg", cv2.IMREAD_GRAYSCALE)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

# Detect blobs.
keypoints = detector.detect(image)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
# the circle corresponds to the size of blob
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 255, 255),
                          cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# Show keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

#The function cv2.drawKeypoints takes the following arguments:
# cv2.drawKeypoints(input image, keypoints, blank_output_array, color, flags)
# flags:
# cv2.DRAW_MATCHES_FLAGS_DEFAULT
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
# cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
# cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS


