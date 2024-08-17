import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array(['A','B','C','D'])
y_axis=np.array([10,30,40,20])

plt.bar(x_axis,y_axis,color='k',width=0.5)  #default width is 0.8
plt.show()