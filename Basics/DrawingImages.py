import cv2
import numpy as np

# Create a black image
image = np.zeros((512,512,3), np.uint8)

# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Black Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Drawing a line
# Draw a diagonal blue line of thickness of 5 pixels
image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511,511), (255,127,0), 5) # image, start, end, color rgb, thickness
cv2.imshow("Blue Line", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Rectangle
# Draw a Rectangle in
image = np.zeros((512,512,3), np.uint8)

cv2.rectangle(image, (100,100), (300,250), (127,50,127), 5) # -1 instead of 5 at the end would fill the rectangle with the color
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Circle
image = np.zeros((512,512,3), np.uint8)

cv2.circle(image, (350, 350), 100, (15,75,50), -1) # cv2.circle(image, center, radius, color, fill)
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Polygon
image = np.zeros((512,512,3), np.uint8)

# Let's define four points
pts = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32)  # specify points to draw lines between them. can add as many as needed

# Let's now reshape our points in form  required by polylines
pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True, (0,0,255), 3)
cv2.imshow("Polygon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# TEXT
image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)
# FONTS AVAILABLE:
# FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
# FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX
# FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
# FONT_HERSHEY_SCRIPT_SIMPLEX
# FONT_HERSHEY_SCRIPT_COMPLEX