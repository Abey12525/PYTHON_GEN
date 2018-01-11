# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 19:21:15 2017

@author: ARH
"""

#suppport vector machine with sklearn


import numpy as np 
from sklearn import cross_validation , svm
import pandas as pd

df = pd.read_csv('dataset_bcancer.txt')
df.replace('?',-99999,inplace=True)
df.drop(['A1'],1,inplace=True)


x = np.array(df.drop(['class'],1))
y = np.array(df['class'])

x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)
clf=svm.SVC()
clf.fit(x_train,y_train)
accuracy=clf.score(x_test,y_test)
print(accuracy)

example_measures = ([[2,3,1,2,2,4,1,2,2],[5,3,3,3,2,3,4,4,1]])
example_measures = np.array(example_measures)
example_measures = example_measures.reshape(2,-1)
pr = clf.predict(example_measures)
print(pr)

