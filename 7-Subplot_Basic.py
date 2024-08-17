import matplotlib.pyplot as plt
import numpy as np

x_axis=np.array([0,1,2,3])
y_axis=np.array([3,7,2,5])

plt.subplot(2,3,1)
plt.plot(x_axis,y_axis)
plt.title("First Subplot")

x_axis=np.array([0,1,2,3])
y_axis=np.array([1,3,5,7])

plt.subplot(2,3,2)
plt.plot(x_axis,y_axis)
plt.title("Second Subplot")

x_axis=np.array([0,1,2,3,4])
y_axis=np.array([3,4,5,6,7])

plt.subplot(2,3,3)
plt.plot(x_axis,y_axis)
plt.title("Third Subplot")

x_axis=np.array([0,1,2,3])
y_axis=np.array([7,5,3,1])

plt.subplot(2,3,4)
plt.plot(x_axis,y_axis)
plt.title("Fourth Subplot")

x_axis=np.array([0,1,2,3])
y_axis=np.array([1,2,3,4])

plt.subplot(2,3,5)
plt.plot(x_axis,y_axis)
plt.title("Fifth Subplot")

x_axis=np.array([0,1,2,3])
y_axis=np.array([10,5,8,1])

plt.subplot(2,3,6)
plt.plot(x_axis,y_axis)
plt.title("Sixth Subplot")

plt.suptitle("My Subplot")
plt.show()