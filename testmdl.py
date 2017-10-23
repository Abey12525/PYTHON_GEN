from sklearn.tree import DecisionTreeClassifier as dt
x=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],
[177,70,40],[155,55,37],[171,75,42],[181,85,43]]

y=['m','m','f','f','m','m','f','f','f','m','m']

clf = dt()

clf.fit(x,y)

p=clf.predict([[190,70,43]])
if(p == 'm'):
	print("prediction = MALE")
else:
	print("prediction = FEMALE")

