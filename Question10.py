# This is a sample Python script.

import numpy as nm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
X = nm.array([[1, 0], [2, 0], [3, 0], [6, 0], [6, 0], [7, 0], [10, 0], [11, 0]])
print("Dataset : \n", X, "\n Size: ", len(X))
y = nm.array([0, 0, 1, 1, 1, 0, 0, 0])
print("\n Clas label for the datasets A  B:", y)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=0, shuffle=False)
print("\nTraining Data A: \n", x_train)
print("\n Training Data label B", y_train)
# feature Scaling-used to normalize the range of independent variables or features of data. .
# i.e.to standardize the data prior to performing classification
stand_scalar = StandardScaler()
x_train = stand_scalar.fit_transform(x_train)
x_test = stand_scalar.transform(x_test)
# Initialising KNN Classifier with value 3
classifier = KNeighborsClassifier(n_neighbors=3)
# Fitting the data to classifier
classifier.fit(x_train, y_train)
# Predict Labels for x-test data
y_pred = classifier.predict(x_test)
print('\nPredicted Classs labels for testing data B:', y_pred)
# Confusion matrix with tested data
confusion_matrix_result = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix\n", confusion_matrix_result)

# total P+N can be calculated using sum(sum(conf_matrix))
total_value = sum(sum(confusion_matrix_result))
# Accuracy TN+TP / P+N
accuracy = (confusion_matrix_result[0, 0] + confusion_matrix_result[1, 1]) / total_value
print('\nAccuracy : ', accuracy)

# Sensitivity TP/(TP+FN)
sensitivity = confusion_matrix_result[1, 1] / (confusion_matrix_result[1, 0] + confusion_matrix_result[1, 1])
print('Sensitivity : ', sensitivity)

# Specificity TN/(TN+FP)
specificity = confusion_matrix_result[0, 0] / (confusion_matrix_result[0, 0] + confusion_matrix_result[0, 1])
print('Specificity : ', specificity)