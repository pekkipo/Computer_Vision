# Live sketch using web camera

import cv2
import numpy as np


# Our sketch generating function
def sketch(image):

    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur.
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    # Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0) # using a webcam

while True:
    ret, frame = cap.read()  # puls an image from the webcam. Loop is required. Loop runs continuosly thus
    cv2.imshow('Our Live Sketcher', sketch(frame)) # then at the rate of frame rate of the webcam the image is passed
    # into a function sketch
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        # waits for the enter key to be pushed in order to stop streaming
        break

# Release camera and close windows
# Necessary!
cap.release()
cv2.destroyAllWindows()