import matplotlib.pyplot as plt
import numpy as np

x=np.array([25,10,20,45])
vote=np.array(['Team A','Team B','Team C','Team D'])
mycolors=np.array(['g','b','r','k'])
myExplode=np.array([0.2,0,0.1,0])

plt.pie(x,labels=vote,startangle=0,explode=myExplode,shadow=True,colors=mycolors)
plt.show()