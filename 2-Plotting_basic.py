import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array([1,9])  #this is horizontal axis
y_axis=np.array([5,12]) #this is vertical axis

#plt.plot(x_axis,y_axis) #The plot function use to draw points in a diagram

#plt.plot(x_axis,y_axis, 'o')    #by using this 'o' parameters,it just draw to point in the diagram
                                #this point is called marker

#####Multiple point
x_axis=np.array([1,3,5,7,9])
y_axis=np.array([5,10,15,7,13])
#plt.plot(x_axis, y_axis)

####Default x points
y_axis=np.array([3,5,9,6,7,1])
plt.plot(y_axis)    #basically when we pass only y axis and not pass x axis then automatically it pass x axis values and starts from 0,1,2.....
plt.show()