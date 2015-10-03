# Machine learning script

import numpy as np									# Numpy for fast arrays
from sklearn.neighbors import KNeighborsClassifier	# Nearest Neighbor Classifier

Data = np.loadtxt("output.txt", unpack="False")		# Training dataset
Test = np.loadtxt("output2.txt", unpack="False")	# Testing dataset

Test = np.transpose(Test)       # Transpose data into rows of data sets
Data = Data.transpose()         # Same idea
test = Test[:, :-1]             # Data is everything but the last entry of the row
X = Data[:,:-1]                 # Data is everything but the last entry of the row
y = Data[:, -1]                 # The last entry of each row is the class

model = KNeighborsClassifier(n_neighbors=3)     # Construct Neighbor model
model.fit(X,y)                                  # Teach the model what is up
results =  model.predict(test)                  # Test the model against the test data
print results                                   # Print the results

#   << Save to Pickel file>>

import pickle
from sklearn.externals import joblib

joblib.dump(model, 'model.pkl')         # Save model to pickle file
                             # Load the model again with clf=joblib.load('model.pkl')
