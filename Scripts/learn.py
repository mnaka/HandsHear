# Machine learning script
import sys, os, thread, time, pickle
import numpy as np									# Numpy for fast arrays
from sklearn.neighbors import KNeighborsClassifier	# Nearest Neighbor Classifier
# sys.path.insert(0, os.path.join('..', '..'))
# import pyttsx
from sklearn.externals import joblib
from sklearn import svm, datasets

Data = np.loadtxt("./datasets/test2.dat", unpack="False")
Data = Data.transpose()
X = Data[:,:-1]
y = Data[:, -1]
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X,y)
joblib.dump(neigh, 'model101.pkl')
