# Machine learning script

import numpy as np									# Numpy for fast arrays
from sklearn.neighbors import KNeighborsClassifier	# Nearest Neighbor Classifier

Data = np.loadtxt("output.txt", unpack="False")		# Training dataset
Test = np.loadtxt("output2.txt", unpack="False")	# Testing dataset
Test = np.transpose(Test)
Data = Data.transpose()
test = Test[:, :-1]
X = Data[:,:-1]
y = Data[:, -1]

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X,y)
results =  neigh.predict(test)
print results
