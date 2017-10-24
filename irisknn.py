import numpy as np
from sklearn import neighbors, datasets

# import some data to play with
iris = datasets.load_iris()
X = iris.data # we only take the first two features. 
Y = iris.target

from sklearn.cross_validation import train_test_split as ts
x_train,x_test,y_train,y_test=ts(X,Y,test_size=.2)
print(x_train)
print("\n")
print(x_test)
print("\n")
print(y_train)
print("\n")
print(y_test)
# step size in the mesh

knn=neighbors.KNeighborsClassifier()

# we create an instance of Neighbours Classifier and fit the data.
clf=knn.fit(x_train, y_train)

p=clf.predict(x_test)

from sklearn.metrics import accuracy_score

print("Accuracy = ",accuracy_score(y_test,p))