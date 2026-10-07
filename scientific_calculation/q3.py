import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,15,10)
y=x**2
fig ,ax=plt.subplots()
ax.plot(x,y)
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_title("plotting graph")
plt.show()