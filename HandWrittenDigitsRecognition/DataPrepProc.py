
# Info about the training data sety
    # 5000 samples, table 50 x 100 images, each digit image is 20x20 pixels
    # Grayscale with black background



# Data pre-processing
    # 500 samples of each digit with 5 rows of 100 samples
    # Each character is 20x20 pixels
    # Use numpy array 50x100x20x20
    # i.e. 50 columns, 100 rows, 20 layers and 20 layers on top of that
    # we flatten that 20x20 array, i.e. we have 20 rows and 20 columns, we append each row to the end of the first
    # thus having 1 row and 400 columns

    # Split training data into 2 segments:
    #     70 % training data - feed into a model and train the model
    #     30 % test data - use a test set to evaluate the model


import numpy as np
import cv2

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
knn = cv2.KNearest()
knn.train(train, train_labels)
ret, result, neighbors, distance = knn.find_nearest(test, k=3)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0 / result.size)
print("Accuracy is = %.2f" % accuracy + "%")
