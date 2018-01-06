# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 19:21:15 2017

@author: ARH
"""

#linear_regression - create a model that best fit our data  
#classification - create a model that divides out data 

# Will allways a odd number grater than the number of groups present 
# confidence - by how much % closser to the grater number class 

#Euclidean distance - finding the closseness to the different class points [as the dataset grows efficency declines]



import numpy as np 
from sklearn import cross_validation , neighbors
import pandas as pd

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except(TypeError, ValueError):
        pass
    return False
    
def replace_de(x):
	for i in range(len(x)):
		for j in range(15):
			if not is_number(x[i,j]):
				if(len(x[i,j])<=2):
					replace=0
					for oj in range(len(x[i,j])):
						replace=ord(x[i,j][oj])+replace
					x[i,j]=replace
					
	
df=pd.read_csv('approval.txt')
df.replace('?',-99999,inplace=True)
df.replace('+',1,inplace=True)
df.replace('-',0,inplace=True)
x = np.array(df.drop(['class'],1))
y = np.array(df['class'])
#df.drop(['A1'],1,inplace=True)
replace_de(x)

for i in range(len(x)):
	for j in range(15):
		x[i,j]=float(x[i,j])

acc=[]

for i in range(25):
	x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)
	clf=neighbors.KNeighborsClassifier()
	clf.fit(x_train,y_train)
	accuracy=clf.score(x_test,y_test)
	acc.append(accuracy)
	
print("Sklearn_Accuracy :",sum(acc)/len(acc))	

#example_measures = ([[2,3,1,2,2,4,1,2,2],[5,3,3,3,2,3,4,4,1]])
#example_measures = np.array(example_measures)
#example_measures = example_measures.reshape(2,-1)
#pr = clf.predict(example_measures)
#print(pr)
