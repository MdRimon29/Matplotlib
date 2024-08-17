import matplotlib.pyplot as plt
import numpy as np

y_axis=np.array([3,7,4,10,1])

plt.plot(y_axis,marker='*',mfc='k',ms='10',ls=':',c='g',lw='2') #ls means linestyle.it can be dotted(:),dashed(--),dashdot(-.),solid(-) or none
                                                                #c means the color of the line
                                                                #lw means line width
#plt.show()

x_axis1=np.array([1,2,3,4])
x_axis2=np.array([1,3,5,7])
y_axis1=np.array([3,5,7,1])
y_axis2=np.array([1,10,4,8])

plt.plot(x_axis1,y_axis1)
plt.plot(x_axis2,y_axis2)
plt.show()  #how many line?total number of plt.plot()