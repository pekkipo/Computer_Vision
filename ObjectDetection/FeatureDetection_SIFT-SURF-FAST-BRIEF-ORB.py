# See the corresponding bookmark
# SIFT and SURF - great but patented and not easily available in OpenCV 3.x
# Alternatives: FAST, BRIEF and ORB (combination of FAST and BRIEF). FAST used for real time applications

# Main scheme of using these in OpenCV
# Create detector - input image into a detector - obtain key points - draw key points


import cv2
import numpy as np

image = cv2.imread('../images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # SIFT
# # http://www.inf.fu-berlin.de/lehre/SS09/CV/uebungen/uebung09/SIFT.pdf
# #Create SIFT Feature Detector object
# sift = cv2.SIFT()
#
# #Detect key points
# keypoints = sift.detect(gray, None)
# print("Number of keypoints Detected: ", len(keypoints))
#
# # Draw rich key points on input image
# image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# cv2.imshow('Feature Method - SIFT', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# # SURF
# # http://www.vision.ee.ethz.ch/~surf/eccv06.pdf
# #Create SURF Feature Detector object
# surf = cv2.SURF()
#
# # Only features, whose hessian is larger than hessianThreshold are retained by the detector
# surf.hessianThreshold = 500
# keypoints, descriptors = surf.detectAndCompute(gray, None)
# print "Number of keypoints Detected: ", len(keypoints)
#
# # Draw rich key points on input image
# image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# cv2.imshow('Feature Method - SURF', image)
# cv2.waitKey()
# cv2.destroyAllWindows()


# FAST
# https://www.edwardrosten.com/work/rosten_2006_machine.pdf
# http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV1011/AV1FeaturefromAcceleratedSegmentTest.pdf

# Create FAST Detector object
fast = cv2.FastFeatureDetector_create()

# Obtain Key points, by default non max suppression is On
# to turn off set fast.setBool('nonmaxSuppression', False)
keypoints = fast.detect(gray, None)
print "Number of keypoints Detected: ", len(keypoints)

out_im = image.copy()
# Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints, out_im, (0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - FAST', image)
cv2.waitKey()
cv2.destroyAllWindows()


# # # BRIEF
# # http://cvlabwww.epfl.ch/~lepetit/papers/calonder_pami11.pdf
#
# image = cv2.imread('../images/input.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Create FAST detector object
# fast = cv2.FastFeatureDetector_create()
#
# # Create BRIEF extractor object
# brief = cv2.DescriptorExtractor("BRIEF")  # doesn't work!
# #DescriptorExtractor_create("BRIEF")
#
#
# # Determine key points
# keypoints = fast.detect(gray, None)
#
# # Obtain descriptors and new final keypoints using BRIEF
# keypoints, descriptors = brief.compute(gray, keypoints)
# print "Number of keypoints Detected: ", len(keypoints)
#
# # Draw rich keypoints on input image
# image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# cv2.imshow('Feature Method - BRIEF', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ORB
# http://www.willowgarage.com/sites/default/files/orb_final.pdf


image = cv2.imread('../images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create ORB object, we can specify the number of key points we desire
orb = cv2.ORB_create()

# Determine key points
keypoints = orb.detect(gray, None)

# Obtain the descriptors
keypoints, descriptors = orb.compute(gray, keypoints)
print("Number of keypoints Detected: ", len(keypoints))

out_im = image.copy()

# Draw rich keypoints on input image
image = cv2.drawKeypoints(image, keypoints, out_im, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - ORB', image)
cv2.waitKey()
cv2.destroyAllWindows()