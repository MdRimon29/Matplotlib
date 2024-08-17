import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y_axis=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors=np.array([10,20,30,40,50,55,60,70,75,80,85,90,100])
sizes=np.array([10,20,30,40,130,120,60,80,50,70,90,100,110])

#plt.scatter(x_axis,y_axis,c=colors,s=sizes,alpha=0.6) #color c can can change the color for the dots
                                                    #size s can change the size of colordots
                                                    #using alpha for adjust transparency our colordots
#plt.colorbar()  #it just add a colorbar in our figure

x_axis = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y_axis = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

#plt.scatter(x_axis,y_axis,color="Blue")

x_axis=np.random.randint(10,size=20)    #all size must be same,size means array size,10 means the range of random value
y_axis=np.random.randint(100,size=20)
colors=np.random.randint(100,size=20)
sizes=5*np.random.randint(100,size=20)

plt.scatter(x_axis,y_axis,c=colors,s=sizes,alpha=0.6)
plt.colorbar()

plt.show()