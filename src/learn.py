import numpy as np

from sklearn.neighbors import KNeighborsClassifier

Data = np.loadtxt("output.txt", unpack="False")
Test = np.loadtxt("output2.txt", unpack="False")
Test = np.transpose(Test)
test = Test[:, :-1]
Data = Data.transpose()
X = Data[:,:-1]
y = Data[:, -1]

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X,y)
results =  neigh.predict(test)
print results
