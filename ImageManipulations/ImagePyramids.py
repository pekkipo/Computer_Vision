import cv2

image = cv2.imread('images/input.jpg')

smaller = cv2.pyrDown(image) # twice as small
larger = cv2.pyrUp(smaller) # twice as big

cv2.imshow('Original', image )

cv2.imshow('Smaller ', smaller )
cv2.imshow('Larger ', larger )
cv2.waitKey(0)
cv2.destroyAllWindows()