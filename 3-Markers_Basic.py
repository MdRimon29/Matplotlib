import matplotlib.pyplot as plt
import numpy as np

y_axis=np.array([1,2,10,4,7])

#plt.plot(y_axis,marker='o') #we can use keyword argument 'marker' to specified each point with specific marker

#plt.plot(y_axis,marker='*')

#plt.plot(y_axis, '*--g') #the syntax is marker|line|color and this is called format string

plt.plot(y_axis,marker='*',ms=20, mec='b',mfc='g')      #here ms means marker size.
                                                        #here mec means marker edge color
                                                        #here mfc means marker face color
                                                        #we can also use hexadecimal color code for marker face and edge color



plt.show()