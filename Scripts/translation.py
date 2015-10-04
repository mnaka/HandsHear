# Machine learning script
import sys, os, thread, time, pickle
import numpy as np									# Numpy for fast arrays
from sklearn.neighbors import KNeighborsClassifier	# Nearest Neighbor Classifier
# sys.path.insert(0, os.path.join('..', '..'))
# import pyttsx
from sklearn.externals import joblib
from sklearn import svm, datasets
translate = {101:"a", 102:"b", 103:"c", 104:"d", 105:"e", 106:"f", 107:"g",
108:"h", 109:"i", 110:"j", 111:"k", 112:"l", 113:"m", 114:"n", 115:"o",
116:"p", 117:"q", 118:"r", 119:"s", 120:"t", 121:"u", 122:"v", 123:"w",
124:"x", 125:"y", 126:"z"};

Test = np.loadtxt("./datasets/test.dat", unpack="False")	# Testing dataset
Test = np.transpose(Test)
test = Test[:, :-1]
neigh = joblib.load('model101.pkl')
results_Array =  neigh.predict(test)
results = []
for i in range (0,len(results_Array)):
    results.append(translate[results_Array[i]])
results="".join(results);
print results;
