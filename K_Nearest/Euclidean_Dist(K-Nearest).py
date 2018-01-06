# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:15:13 2017

@author: ARH
"""
# root(sum of i=1 to n (Qi-Pi)^2)


import math as m
#import matplotlib.pyplot as plt 
#from matplotlib import style
from collections import Counter
import warnings as wr
import numpy as np
import time 
import pandas as pd 
import random
from sklearn import cross_validation , neighbors 
#style.use('fivethirtyeight')

#dataset={'k':[[1,2],[3,4],[2,1]],'r':[[6,5],[7,7],[8,5]]}
#for char in 'abcdefghijklmnopqrstuvwxyz':
def math_dist(a,b):
    return m.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
   
   
def numpy_dist(a,b):
	 return np.linalg.norm(a-b)
	 
	 
def k_nearest_neighbours(data,predict,k=3):
	if len(data) >= k :
		warning.warn("K is set to value less than total voting group dude !!!!")
	distances = []
	for group in data:
		for features in data[group]:
			distances.append([numpy_dist(np.array(features),np.array(predict)),group])
	votes=[i[1]  for i in sorted(distances) [:k]]
	vote_result=Counter(votes).most_common(1)[0][0]
	confidence=Counter(votes).most_common(1)[0][1]/k
	return vote_result,confidence
	
	
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
#df.drop(['A1'],1,inplace=True)
x = np.array(df)
replace_de(x)

for i in range(len(x)):
	for j in range(16):
		x[i,j]=float(x[i,j])

df=pd.DataFrame(x)
#df.to_csv('tt.csv')
#np.savetxt('test.csv',x,delimiter=' ')

y=x
accuracy=[]
for i in range(25):
	x=y
	random.shuffle(x)
	test_size = 0.2
	train_set = { 1: [],0: []}
	test_set={1: [],0: []}
	train_data=x[:-int(test_size*len(x))]
	test_data=x[-int(test_size*len(x)):]

	for i in train_data:
		train_set[i[-1]].append(i [ : -1])
		
	for i in test_data:
		test_set[i[-1]].append(i [ : -1])
		
	correct = 0 
	total = 0

	for group in test_set:
		for data in test_set[group]:
			vote,c = k_nearest_neighbours(train_set,data,k=4)
			if group == vote:
				correct +=1
			total += 1
	accuracy.append(correct/total)
print('Home made Accuracy :',sum(accuracy)/len(accuracy))



#eculidean_distance = m.sqrt((plot1[0]-plot2[0])**2+(plot1[1]-plot2[1])**2)
"""
for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0],ii[1],s=100,color=i)
"""



#result=k_nearest_neighbours(x,new_features,k=3)
"""
[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1],color=result)
plt.show()
"""

