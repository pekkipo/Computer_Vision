import cv2
import numpy as np
import PrepareInputImage as prep

### Processing and Training

# Info about the training data sety
    # 5000 samples, table 50 x 100 images, each digit image is 20x20 pixels
    # Grayscale with black background



# Data pre-processing
    # 500 samples of each digit with 5 rows of 100 samples
    # Each character is 20x20 pixels
    # Use numpy array 50x100x20x20
    # i.e. 50 columns, 100 rows, 20 layers and 20 layers on top of that
    # flatten that 20x20 array, i.e. have 20 rows and 20 columns, thus append each row to the end of the first
    # thus having 1 row and 400 columns

    # Split training data into 2 segments:
    #     70 % training data - feed into a model and train the model
    #     30 % test data - use a test set to evaluate the model


# Digits dataset
image = cv2.imread('../images/digits.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
small = cv2.pyrDown(image)
cv2.imshow('Digits Image', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Split the image to 5000 cells, each 20x20 size
# This gives us a 4-dim array: 50 x 100 x 20 x 20
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# Convert the List data type to Numpy Array of shape (50,100,20,20)
x = np.array(cells)
print ("The shape of the cells array: " + str(x.shape))

# Split the full data set into two segments
# One will be used fro Training the model, the other as a test data set
# rehsape -1 400 flattens the array
train = x[:,:70].reshape(-1,400).astype(np.float32) # Size = (3500,400)
test = x[:,70:100].reshape(-1,400).astype(np.float32) # Size = (1500,400)

# Create labels for train and test data
k = [0,1,2,3,4,5,6,7,8,9] # 10 digits
train_labels = np.repeat(k,350)[:,np.newaxis] # 350x10 = 3500
test_labels = np.repeat(k,150)[:,np.newaxis]  # 1500

# Initiate kNN, train the data, then test it with test data for k=3
# knn = cv2.KNearest()
# knn.train(train, train_labels)
# ret, result, neighbors, distance = knn.find_nearest(test, k=3)

# OpenCV 3 api for KNearest
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbors, distance = knn.findNearest(test, k=3)

# Now check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0 / result.size)
print("Accuracy is = %.2f" % accuracy + "%")

### Recognition

image = cv2.imread('../images/numbers.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image", image)
cv2.imshow("gray", gray)
cv2.waitKey(0)

# Blur image then find edges using Canny
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("blurred", blurred)
cv2.waitKey(0)

edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("edged", edged)
cv2.waitKey(0)

# Fint Contours
_, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort out contours left to right by using their x cordinates
contours = sorted(contours, key=prep.x_cord_contour, reverse=False)

# Create empty array to store entire number
full_number = []

# loop over the contours
for c in contours:
    # compute the bounding box for the rectangle
    (x, y, w, h) = cv2.boundingRect(c)

    # cv2.drawContours(image, contours, -1, (0,255,0), 3)
    # cv2.imshow("Contours", image)

    if w >= 5 and h >= 25:
        roi = blurred[y:y + h, x:x + w]
        ret, roi = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY_INV)
        squared = prep.makeSquare(roi)
        final = prep.resize_to_pixel(20, squared)
        cv2.imshow("final", final)
        final_array = final.reshape((1, 400))
        final_array = final_array.astype(np.float32)
        ret, result, neighbours, dist = knn.findNearest(final_array, k=1)
        number = str(int(float(result[0])))
        full_number.append(number)
        # draw a rectangle around the digit, the show what the
        # digit was classified as
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, number, (x, y + 155),
                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
        cv2.imshow("image", image)
        cv2.waitKey(0)

cv2.destroyAllWindows()
print ("The number is: " + ''.join(full_number))

