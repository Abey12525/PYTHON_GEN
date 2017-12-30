#y=mx+c
#m=mean(x).mean(y)-mean(xy)/mean(x)^2-mean(x^2)
#c=mean(y)-m*mean(x) 
from statistics import mean
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
import random as r 

style.use('fivethirtyeight')
#xs =np.array([1,2,3,4,5,6],dtype=np.float64)
#ys =np.array([5,4,6,5,6,7],dtype=np.float64)
def create_dataset(data_points,variance,step=2,correlation=False):
    val=1
    ys=[]
    for i in range(data_points):    
        y=val+r.randrange(-variance,variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val+=step
        elif correlation and correlation == 'neg':
            val-=step
    
    xs=[i for i in range(len(ys))]       
    return np.array(xs,dtype=np.float64),np.array(ys,dtype=np.float64)
   
    
def best_fit_slop_intercept(xs,ys):
	m=( ((mean(xs)*mean(ys))-mean(xs*ys))/
	((mean(xs)*mean(xs))-mean(xs*xs)))
	
	b=mean(ys)-m*mean(xs)
	
	return m,b
	
def squared_error(ys_orig,ys_line):
		return sum((ys_line-ys_orig)**2)
		
def r_squre(ys_orig,ys_line):
    y_mean_line=[mean(ys_orig) for y in ys_line]
    #ys_line is the line created by the equation y=mx+b
    #values in y_mean_line are equal ie[1,1,1,1,1]or[5.5.5.5.5.5]  
    squred_error_regr=squared_error(ys_orig,ys_line)    
    squred_error_y_mean=squared_error(ys_orig,y_mean_line)	
    return 1-(squred_error_regr/squred_error_y_mean)


xs,ys=create_dataset(40,30,4,correlation='pos')
print(ys)	
m,b=best_fit_slop_intercept(xs,ys)

regression_line=[(m*x)+b for x in xs]
r_squred=r_squre(ys,regression_line)
print(r_squred)

plt.plot(xs,ys)
plt.plot(xs,regression_line)
plt.show()
print(m,b)

