from sklearn.tree import DecisionTreeClassifier as dt
from sklearn.datasets import load_iris as ir
import numpy as np

iris = ir()

fet=iris.data
lab=iris.target

from sklearn.cross_validation import train_test_split as ts
x_train,x_test,y_train,y_test=ts(fet,lab,test_size=.3)

clf = dt()
clf.fit(x_train,y_train)


p=clf.predict(x_test)

from sklearn.metrics import accuracy_score

print("Accuracy = ",accuracy_score(y_test,p))