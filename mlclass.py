from sklearn.tree import DecisionTreeClassifier as dt

features=[[140,0],[120,0],[150,1],[170,1]]
""" 0 - smooth 1 - bumpy """
lb=[0,0,1,1]
""" 0 - apple 1 - orange """
#init tree
clf = dt()
#itrates through data
clf.fit(features,lb)

p = clf.predict([[160,1]])
print(p)
