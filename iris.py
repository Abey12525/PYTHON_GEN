from sklearn.datasets import load_iris as ir
import numpy as np 
from sklearn.tree import DecisionTreeClassifier as dt

"""	0 - sat
	1 - ves
	2 - vt
"""
iris=ir()
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data[0])
#print(iris.target[0])

x=[0,50,100]

xtrain = np.delete(iris.data,x,axis=0)
ytrain = np.delete(iris.target,x)

xtest = iris.data[x]
ytest = iris.target[x]

clf = dt()
clf.fit(xtrain,ytrain)

print(ytest)
print("prediction =  ",clf.predict(xtest))

