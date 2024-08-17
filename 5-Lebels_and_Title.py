import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array([10,20,30,40,50,60,70,80])
y_axis=np.array([5,10,15,30,25,35,30,25])

plt.plot(x_axis,y_axis)

font1={"color":'red','size':20}     #we can use fontdict parameter to set properties for title and labels
font2={'color':'green','size':15}

plt.title("Details in a football match",loc="left",fontdict=font1)      #title for the graph
                                                                        #here loc means the location of title,left or right or center(default) 
plt.xlabel("Running speed",fontdict=font2) #name for the x axis
plt.ylabel("Time spend in a match",fontdict=font2) #name for the y axis

plt.show()