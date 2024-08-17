import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array([10,20,30,40,50,60,70,80])
y_axis=np.array([5,10,15,30,25,35,30,25])

plt.plot(x_axis,y_axis)

plt.title("Details in a football match")
plt.xlabel("Running speed")
plt.ylabel("Time spend in a match")

#plt.grid(axis="y")
#plt.grid(axis="x")
#plt.grid()  #in this case grid draw in both axis
plt.grid(axis="y",color='g',ls=':',lw=1) #axis means the axis of grid,lw means lineweidth of grid,ls means linestyle of grid,color means the color of grid

plt.show()