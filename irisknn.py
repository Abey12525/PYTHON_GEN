from scipy.spatial import distance as d 
def udistance(t,tr):
	#returns the distance btw test and train set
	return d.euclidean(t,tr)
###############################################

class myKNN():
	def fit(self,X_train,Y_train):
		self.x_train=X_train
		self.y_train=Y_train


	def predict(self,X_test):
		predictions = []
		for row in X_test:
			label=self.closest(row)
			predictions.append(label)
		return predictions

	
	def closest(self,row):
	 	lo_distance=udistance(row,self.x_train[0])
	 	idx=0
	 	for i in range(1,len(self.x_train)):
	 		if(udistance(row,self.x_train[i])<lo_distance):
	 			lo_distance=udistance(row,self.x_train[i])
	 			idx=i
	 	return self.y_train[idx]

###############################################################

import numpy as np
from sklearn import neighbors, datasets

# import data
iris = datasets.load_iris()
X = iris.data  
Y = iris.target

from sklearn.cross_validation import train_test_split as ts
x_train,x_test,y_train,y_test=ts(X,Y,test_size=.2)


clf=myKNN()
# we create an instance of myKNN and fit the data.
clf.fit(x_train,y_train)
p=clf.predict(x_test)

from sklearn.metrics import accuracy_score
for i in range(len(p)):
	print("test set = ",x_test[i,:],end=" ")
	print("label = ",y_test[i],end=" ")
	print("prediction =",p[i])

print("Accuracy = ",accuracy_score(y_test,p))