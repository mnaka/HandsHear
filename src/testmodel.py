from sklearn.externals import joblib
import pickle
import numpy as np

Test = np.loadtxt("./datasets/testdata.dat", unpack="False")
Test = np.transpose(Test)
test_data = Test[:, :-1]
expected_result = Test[:, -1]

estimator = joblib.load("./model/estimator.pkl")

result = estimator.predict(test_data)

print "Expected Result: "
print expected_result
print "Model gives: "
print result
