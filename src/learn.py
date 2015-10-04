# Machine learning script

import numpy as np									# Numpy for fast arrays
from sklearn.ensemble import RandomForestClassifier	# Nearest Neighbor Classifier
from sklearn.pipeline import Pipeline               # Estimator pipeline
from sklearn.grid_search import GridSearchCV        # Grid Search
from sklearn import decomposition

Data = np.loadtxt("./datasets/learndata.dat", unpack="False")		# Training dataset
Test = np.loadtxt("./datasets/testdata.dat", unpack="False")    	# Testing dataset

Test = np.transpose(Test)       # Transpose data into rows of data sets
Data = Data.transpose()         # Same idea

test = Test[:, :-1]             # Data is everything but the last entry of the row
X = Data[:,:-1]                 # Data is everything but the last entry of the row
y = Data[:, -1]                 # The last entry of each row is the class

model = RandomForestClassifier(n_estimators=25)     # Construct Neighbor model
pca = decomposition.PCA()
pipe = Pipeline(steps=[('pca', pca), ('model', model)])
pca.fit(X)

# <<< Plot the PCA spectrum >>>
import matplotlib.pyplot as plt
plt.plot(pca.explained_variance_)
plt.axis('tight')
plt.show()

n_components = [3, 4, 5, 6, 10, 15, 20]
n_esti = [5, 10, 15, 20, 25, 50]

estimator = GridSearchCV(pipe, dict(pca__n_components=n_components, model__n_estimators=n_esti))
estimator.fit(X,y)

model.fit(X,y)                                  # Teach the model what is up
results =  model.predict(test)                  # Test the model against the test data
print "Classifier results:", results            # Print the results
results = estimator.predict(test)
print "Pipeline results:", results

#   << Save to Pickel file>>

import pickle
from sklearn.externals import joblib

joblib.dump(estimator, 'estimator.pkl')         # Save model to pickle file
                             # Load the model again with clf=joblib.load('model.pkl')
